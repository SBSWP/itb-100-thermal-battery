"""
ITB-100 Thermal Battery System Model
=====================================

Comprehensive physics-based model for thermal energy storage analysis.

⚠️  CRITICAL DISCLAIMERS
------------------------

1. **UNVALIDATED MODEL**: No physical prototype has been built or tested.
   Real-world performance may differ significantly from predictions.

2. **KEY ASSUMPTIONS REQUIRING VALIDATION**:
   - SAT chemistry: 1,000+ cycle stability (literature-based, NOT tested)
   - Heat transfer: UA = 111.7 W/K (calculated, NOT measured)
   - Manufacturing costs: Volume estimates (NOT actual quotes)
   - Nucleation: 95%+ success rate (needs experimental verification)

3. **LOCATION-SPECIFIC**: All climate and economic data for Syracuse, NY.
   Adapt parameters for your location (see location_data dict in code).

4. **DATE-SENSITIVE**: Analysis as of October 2025. Market conditions,
   competitor pricing, and regulations will change over time.

APPROPRIATE USE
---------------
✅ Research and conceptual design exploration
✅ Identifying critical questions and testing protocols
✅ Comparing thermal storage alternatives on consistent basis

INAPPROPRIATE USE
-----------------
❌ Final engineering design without physical validation
❌ Financial projections for business plans or funding
❌ Performance guarantees or warranty calculations

For validation testing protocol, see: VALIDATION_TEST.md
For detailed assumptions, see: ITB100_MODEL_DOCUMENTATION.md

Installation
------------
pip install -r requirements.txt

Usage
-----
python itb100_system_model.py --output-dir ./output

Outputs will be saved to specified directory (default: ./output/).

Author: ITB-100 Design Team
Date: October 2025
License: MIT (see LICENSE file)
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple, Dict, List
from datetime import datetime, timedelta
import os
from pathlib import Path
import argparse

# ============================================================================
# SYSTEM SPECIFICATIONS (From Final Design)
# ============================================================================

@dataclass
class ITB100Specs:
    """Fixed design specifications for the ITB-100 thermal battery"""
    
    # Phase Change Material Properties
    T_phase: float = 58.0  # Â°C - SAT phase change temperature
    T_phase_K: float = 331.15  # K
    delta_H_fusion: float = 264.4e3  # J/kg - Latent heat of fusion
    k_sat_solid: float = 0.5  # W/(mÂ·K) - Thermal conductivity (solid)
    k_sat_liquid: float = 0.54  # W/(mÂ·K) - Thermal conductivity (liquid)
    rho_sat_solid: float = 1450  # kg/mÂ³
    rho_sat_liquid: float = 1280  # kg/mÂ³
    cp_sat_solid: float = 2100  # J/(kgÂ·K) - Specific heat (solid)
    cp_sat_liquid: float = 3500  # J/(kgÂ·K) - Specific heat (liquid)
    
    # System Geometry
    M_sat: float = 227.1  # kg - Total SAT mass
    A_hx: float = 26.1  # mÂ² - Total heat exchanger surface area
    delta_sat: float = 0.003  # m - PCM half-thickness (3 mm slabs)
    V_total: float = 0.16  # mÂ³ - Total system volume
    
    # Heat Exchanger
    L_tube: float = 4.0  # m - Total manifold tubing length
    D_tube: float = 0.01905  # m - Tube diameter (3/4")
    N_plates: int = 52  # Number of aluminum plates
    t_plate: float = 0.002  # m - Plate thickness (2 mm)
    k_aluminum: float = 205  # W/(mÂ·K) - Aluminum thermal conductivity
    
    # Hydraulic Properties
    m_dot_design: float = 0.074  # kg/s - Design flow rate (4.4 L/min)
    cp_water: float = 4186  # J/(kgÂ·K) - Water specific heat
    
    # System Performance - Derived from Design Targets
    UA_effective: float = 111.7  # W/K - Overall heat transfer coefficient Ã— Area
                                  # Calculated as Q_target / Delta_T_eff = 2010W / 18K
                                  # Accounts for: tube-plate resistance, plate conduction,
                                  # plate-pouch contact, and SAT conduction
    
    # Performance Targets
    Q_discharge_target: float = 2010  # W - Target discharge power
    Q_charge_target: float = 2780  # W - Average solar charge power
    t_charge_design: float = 6.0  # hours - Design charge window
    t_discharge_design: float = 8.29  # hours - Design discharge duration
    
    # Energy Storage
    E_storage: float = 16.71  # kWh - Total storage capacity
    
    # Economic Parameters
    capital_cost: float = 3500  # $ - Total system cost
    lifetime_cycles: int = 1000  # Design life in charge/discharge cycles
    lifetime_years: float = 10  # Design life in years

# ============================================================================
# THERMAL DYNAMICS MODEL
# ============================================================================

class ThermalBatteryModel:
    """Physics-based model of ITB-100 thermal dynamics"""
    
    def __init__(self, specs: ITB100Specs):
        self.specs = specs
        self.reset_state()
    
    def reset_state(self):
        """Initialize or reset system state"""
        self.T_sat = 20.0  # Â°C - Initial SAT temperature
        self.solid_fraction = 1.0  # Fully solid initially
        self.E_stored = 0.0  # J - Stored energy (relative to fully solid at 20Â°C)
        self.time = 0.0  # s - Simulation time
        
    def get_state_of_charge(self) -> float:
        """Calculate state of charge (0 = empty/solid, 1 = full/liquid)"""
        E_max = self.specs.E_storage * 3.6e6  # Convert kWh to J
        return max(0.0, min(1.0, self.E_stored / E_max))
    
    def get_effective_thermal_conductivity(self) -> float:
        """Calculate effective thermal conductivity based on phase state"""
        k_solid = self.specs.k_sat_solid
        k_liquid = self.specs.k_sat_liquid
        return self.solid_fraction * k_solid + (1 - self.solid_fraction) * k_liquid
    
    def calculate_heat_flux(self, T_water_avg: float) -> float:
        """
        Calculate heat flux between water and SAT
        
        Args:
            T_water_avg: Average water temperature in heat exchanger (Â°C)
        
        Returns:
            q_flux: Heat flux in W/mÂ² (positive = charging, negative = discharging)
        """
        k_eff = self.get_effective_thermal_conductivity()
        delta_T = T_water_avg - self.T_sat
        q_flux = (k_eff / self.specs.delta_sat) * delta_T
        return q_flux
    
    def calculate_power(self, T_water_avg: float) -> float:
        """
        Calculate total heat transfer power
        
        Args:
            T_water_avg: Average water temperature (Â°C)
        
        Returns:
            Q: Power in W (positive = charging, negative = discharging)
        """
        q_flux = self.calculate_heat_flux(T_water_avg)
        Q = q_flux * self.specs.A_hx
        return Q
    
    def step_discharge(self, T_water_in: float, dt: float) -> Tuple[float, float]:
        """
        Simulate one discharge time step
        
        Args:
            T_water_in: Inlet water temperature (Â°C)
            dt: Time step (seconds)
        
        Returns:
            Q_actual: Actual power delivered (W)
            T_water_out: Outlet water temperature (Â°C)
        """
        # Check if battery is depleted (fully solid and below phase temp)
        if self.solid_fraction >= 0.99 and self.T_sat < self.specs.T_phase:
            return 0.0, T_water_in
        
        # If battery is cooler than inlet water, can't discharge
        if self.T_sat <= T_water_in + 0.5:
            return 0.0, T_water_in
        
        # Use simplified LMTD (log mean temperature difference) approach
        # For counter-flow HX: Q = UA * LMTD
        # Simplified: assume outlet approaches SAT temp asymptotically
        
        # Effectiveness-NTU method (simplified)
        NTU = self.specs.UA_effective / (self.specs.m_dot_design * self.specs.cp_water)
        effectiveness = 1 - np.exp(-NTU)  # For single-pass HX
        
        # Maximum possible heat transfer if outlet reached SAT temp
        Q_max = self.specs.m_dot_design * self.specs.cp_water * (self.T_sat - T_water_in)
        
        # Actual heat transfer limited by effectiveness
        Q_actual = effectiveness * Q_max
        Q_actual = max(0.0, Q_actual)
        
        # Calculate outlet temperature
        if Q_actual > 0:
            delta_T_water = Q_actual / (self.specs.m_dot_design * self.specs.cp_water)
            T_water_out = T_water_in + delta_T_water
        else:
            T_water_out = T_water_in
        
        # Update battery state based on energy extracted
        if Q_actual > 0:
            dE = Q_actual * dt
            
            if self.T_sat > self.specs.T_phase + 0.1:
                # Cooling liquid SAT (sensible heat)
                dT = dE / (self.specs.M_sat * self.specs.cp_sat_liquid)
                self.T_sat -= dT
                self.E_stored -= dE
                
                if self.T_sat <= self.specs.T_phase:
                    self.T_sat = self.specs.T_phase
            
            elif self.solid_fraction < 0.99:
                # Phase change (solidification) - this is where most energy comes from
                dm_solidified = dE / self.specs.delta_H_fusion
                self.solid_fraction += dm_solidified / self.specs.M_sat
                self.solid_fraction = min(1.0, self.solid_fraction)
                self.E_stored -= dE
                self.T_sat = self.specs.T_phase  # Stay at phase change temp
            
            else:
                # Fully solid, cooling down - no useful energy
                dT = dE / (self.specs.M_sat * self.specs.cp_sat_solid)
                self.T_sat -= dT
                self.E_stored -= dE
                Q_actual = 0.0  # Don't count sensible cooling as useful output
        
        self.time += dt
        return Q_actual, T_water_out
    
    def step_charge(self, T_water_in: float, dt: float) -> Tuple[float, float]:
        """
        Simulate one charge time step
        
        Args:
            T_water_in: Inlet water temperature from solar collectors (Â°C)
            dt: Time step (seconds)
        
        Returns:
            Q_actual: Actual power absorbed (W)
            T_water_out: Outlet water temperature (Â°C)
        """
        # Check if battery is fully charged
        if self.solid_fraction <= 0.01 and self.T_sat >= self.specs.T_phase + 5:
            return 0.0, T_water_in
        
        # If inlet water is cooler than battery, can't charge
        if T_water_in <= self.T_sat + 0.5:
            return 0.0, T_water_in
        
        # Use effectiveness-NTU method
        NTU = self.specs.UA_effective / (self.specs.m_dot_design * self.specs.cp_water)
        effectiveness = 1 - np.exp(-NTU)
        
        # Maximum possible heat transfer
        Q_max = self.specs.m_dot_design * self.specs.cp_water * (T_water_in - self.T_sat)
        
        # Actual heat transfer
        Q_actual = effectiveness * Q_max
        Q_actual = max(0.0, Q_actual)
        
        # Calculate outlet temperature
        if Q_actual > 0:
            delta_T_water = Q_actual / (self.specs.m_dot_design * self.specs.cp_water)
            T_water_out = T_water_in - delta_T_water
        else:
            T_water_out = T_water_in
        
        # Update battery state
        if Q_actual > 0:
            dE = Q_actual * dt
            
            if self.T_sat < self.specs.T_phase - 0.1:
                # Heating solid SAT (sensible heat)
                dT = dE / (self.specs.M_sat * self.specs.cp_sat_solid)
                self.T_sat += dT
                self.E_stored += dE
                
                if self.T_sat >= self.specs.T_phase:
                    self.T_sat = self.specs.T_phase
            
            elif self.solid_fraction > 0.01:
                # Phase change (melting) - this is where most energy goes
                dm_melted = dE / self.specs.delta_H_fusion
                self.solid_fraction -= dm_melted / self.specs.M_sat
                self.solid_fraction = max(0.0, self.solid_fraction)
                self.E_stored += dE
                self.T_sat = self.specs.T_phase
            
            else:
                # Fully liquid, heating up (superheat)
                dT = dE / (self.specs.M_sat * self.specs.cp_sat_liquid)
                self.T_sat += dT
                self.E_stored += dE
        
        self.time += dt
        return Q_actual, T_water_out

# ============================================================================
# DISCHARGE SIMULATION
# ============================================================================

def simulate_discharge(specs: ITB100Specs, 
                       T_supply: float = 40.0,
                       T_return_target: float = 45.0,
                       dt: float = 60.0) -> Dict:
    """
    Simulate complete discharge cycle
    
    Args:
        specs: System specifications
        T_supply: Supply water temperature to heating load (Â°C)
        T_return_target: Target return temperature (Â°C)
        dt: Time step in seconds
    
    Returns:
        Dictionary with time series results
    """
    model = ThermalBatteryModel(specs)
    
    # Initialize battery to fully charged state
    model.T_sat = specs.T_phase  # At phase change temperature
    model.solid_fraction = 0.05  # Mostly liquid (5% solid to be conservative)
    model.E_stored = specs.E_storage * 3.6e6  # Full charge in Joules
    
    # Storage for results
    time_history = []
    T_sat_history = []
    T_out_history = []
    Q_history = []
    SOC_history = []
    solid_fraction_history = []
    
    # Simulate until battery is depleted
    time = 0.0
    max_time = 12 * 3600  # 12 hour maximum
    
    while time < max_time:
        Q_actual, T_out = model.step_discharge(T_supply, dt)
        
        # Record state
        time_history.append(time / 3600)  # Convert to hours
        T_sat_history.append(model.T_sat)
        T_out_history.append(T_out)
        Q_history.append(Q_actual / 1000)  # Convert to kW
        SOC_history.append(model.get_state_of_charge())
        solid_fraction_history.append(model.solid_fraction)
        
        time += dt
        
        # Stop if battery is depleted or power drops to near zero
        if model.get_state_of_charge() < 0.01 or (Q_actual < 100 and time > 3600):
            break
    
    # Calculate summary statistics
    total_energy_delivered = np.trapz(Q_history, time_history)  # kWh
    avg_power = np.mean(Q_history)  # kW
    duration = time_history[-1] if len(time_history) > 0 else 0  # hours
    
    return {
        'time': np.array(time_history),
        'T_sat': np.array(T_sat_history),
        'T_out': np.array(T_out_history),
        'Q': np.array(Q_history),
        'SOC': np.array(SOC_history),
        'solid_fraction': np.array(solid_fraction_history),
        'total_energy': total_energy_delivered,
        'avg_power': avg_power,
        'duration': duration
    }

# ============================================================================
# CHARGE SIMULATION
# ============================================================================

def simulate_charge(specs: ITB100Specs,
                   solar_profile: np.ndarray,
                   T_collector: np.ndarray,
                   dt: float = 60.0) -> Dict:
    """
    Simulate charge cycle with time-varying solar input
    
    Args:
        specs: System specifications
        solar_profile: Array of solar thermal power available (W) vs time
        T_collector: Array of collector outlet temperatures (Â°C) vs time
        dt: Time step in seconds
    
    Returns:
        Dictionary with time series results
    """
    model = ThermalBatteryModel(specs)
    
    # Initialize battery to depleted state (trigger nucleation first in real system)
    model.T_sat = 20.0
    model.solid_fraction = 1.0
    model.E_stored = 0.0
    
    # Storage for results
    time_history = []
    T_sat_history = []
    T_out_history = []
    Q_history = []
    Q_available_history = []
    SOC_history = []
    solid_fraction_history = []
    
    n_steps = len(solar_profile)
    time = 0.0
    
    for i in range(n_steps):
        Q_available = solar_profile[i]
        T_in = T_collector[i]
        
        # Attempt to charge
        Q_actual, T_out = model.step_charge(T_in, dt)
        
        # Q_actual is limited by battery acceptance rate, not solar availability
        Q_actual = min(Q_actual, Q_available)
        
        # Record state
        time_history.append(time / 3600)
        T_sat_history.append(model.T_sat)
        T_out_history.append(T_out)
        Q_history.append(Q_actual / 1000)  # kW
        Q_available_history.append(Q_available / 1000)  # kW
        SOC_history.append(model.get_state_of_charge())
        solid_fraction_history.append(model.solid_fraction)
        
        time += dt
        
        # Stop if fully charged
        if model.get_state_of_charge() >= 0.99:
            break
    
    total_energy_charged = np.trapz(Q_history, time_history)  # kWh
    avg_power = np.mean(Q_history)  # kW
    duration = time_history[-1] if len(time_history) > 0 else 0
    
    return {
        'time': np.array(time_history),
        'T_sat': np.array(T_sat_history),
        'T_out': np.array(T_out_history),
        'Q': np.array(Q_history),
        'Q_available': np.array(Q_available_history),
        'SOC': np.array(SOC_history),
        'solid_fraction': np.array(solid_fraction_history),
        'total_energy': total_energy_charged,
        'avg_power': avg_power,
        'duration': duration
    }

# ============================================================================
# SOLAR THERMAL SYSTEM MODELING
# ============================================================================

def generate_solar_profile(location: str = "Syracuse_NY",
                          date: str = "2025-01-15",
                          collector_area: float = 12.0,
                          collector_efficiency: float = 0.70) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate realistic solar thermal collector output profile for evacuated tube collectors
    
    Args:
        location: Location identifier
        date: Date string (YYYY-MM-DD)
        collector_area: Total collector area (mÂ²)  
        collector_efficiency: Collector efficiency at operating temperature
    
    Returns:
        time_array: Hours from midnight
        power_array: Thermal power output (W)
        temp_array: Collector outlet temperature (Â°C)
    """
    # Evacuated tube collectors are highly effective even in cold, cloudy conditions
    # Syracuse, NY - January clear day scenario (required for full charge)
    
    # Time array (9 AM to 3 PM, 6 hour useful window)
    time_hours = np.linspace(9, 15, 73)  # 5-minute intervals
    
    # Solar irradiance profile for a good winter day
    # Peak occurs at solar noon (12:00)
    hour_of_day = time_hours
    peak_irradiance = 800  # W/mÂ² (clear winter day, lower angle)
    
    # Gaussian profile centered at noon
    irradiance = peak_irradiance * np.exp(-((hour_of_day - 12)**2) / 4.5)
    
    # Account for winter conditions (but assume a good charging day)
    cloud_factor = 0.85  # 85% of clear-sky (some thin clouds/haze)
    irradiance *= cloud_factor
    
    # Evacuated tube collector output
    # High efficiency maintained even at elevated temperatures
    Q_collector = irradiance * collector_area * collector_efficiency
    
    # Collector outlet temperature 
    T_ambient = -2.0  # Â°C (January in Syracuse)
    
    # Evacuated tubes achieve excellent temperature rise
    # Temperature rises with solar intensity but has a practical upper limit
    normalized_intensity = irradiance / (peak_irradiance * cloud_factor)
    
    # Temperature model: T = T_ambient + f(solar) with stagnation limit
    T_stagnation = 120.0  # Â°C (maximum collector temperature)
    T_rise = (T_stagnation - T_ambient) * (1 - np.exp(-3 * normalized_intensity))
    
    T_collector = T_ambient + T_rise
    
    # Realistic operating range for charging (need to be above 58Â°C phase change)
    T_collector = np.clip(T_collector, 60.0, 95.0)
    
    return time_hours, Q_collector, T_collector

# ============================================================================
# ECONOMIC ANALYSIS
# ============================================================================

class EconomicModel:
    """Economic analysis of thermal battery system"""
    
    def __init__(self, specs: ITB100Specs, location_data: Dict):
        self.specs = specs
        self.location = location_data
    
    def calculate_annual_savings(self, 
                                 cycles_per_year: int = 150,
                                 heat_source: str = "natural_gas") -> Dict:
        """
        Calculate annual operating cost savings
        
        Args:
            cycles_per_year: Number of charge/discharge cycles per year
            heat_source: Alternative heating fuel type
        
        Returns:
            Dictionary with economic metrics
        """
        # Energy delivered per cycle
        energy_per_cycle = self.specs.E_storage  # kWh
        annual_energy = energy_per_cycle * cycles_per_year  # kWh/year
        
        # Cost of alternative heating
        fuel_costs = {
            'natural_gas': 0.80 / 29.3,  # $/kWh (at $0.80/therm, 29.3 kWh/therm)
            'propane': 2.50 / 27.0,  # $/kWh (at $2.50/gallon, 27 kWh/gallon)
            'heating_oil': 3.00 / 40.0,  # $/kWh (at $3.00/gallon, 40 kWh/gallon)
            'electric_resistance': 0.15,  # $/kWh (typical electric rate)
            'heat_pump': 0.15 / 3.0,  # $/kWh (COP = 3.0 at moderate temps)
        }
        
        fuel_cost_per_kwh = fuel_costs.get(heat_source, 0.10)
        
        # Efficiency factors
        furnace_efficiency = 0.90 if 'gas' in heat_source else 1.0
        
        # Annual fuel cost savings
        annual_fuel_savings = (annual_energy / furnace_efficiency) * fuel_cost_per_kwh
        
        # Operating costs (pump electricity)
        pump_power = 50  # W (circulator pump)
        hours_per_cycle = self.specs.t_discharge_design + self.specs.t_charge_design
        annual_pump_energy = pump_power * hours_per_cycle * cycles_per_year / 1000  # kWh
        annual_pump_cost = annual_pump_energy * 0.15  # $ (at $0.15/kWh)
        
        # Net annual savings
        net_annual_savings = annual_fuel_savings - annual_pump_cost
        
        # Simple payback
        simple_payback = self.specs.capital_cost / net_annual_savings  # years
        
        # 10-year NPV (assume 3% discount rate)
        discount_rate = 0.03
        years = np.arange(1, 11)
        cash_flows = net_annual_savings / ((1 + discount_rate) ** years)
        npv_10yr = np.sum(cash_flows) - self.specs.capital_cost
        
        return {
            'annual_energy_delivered': annual_energy,
            'annual_fuel_savings': annual_fuel_savings,
            'annual_pump_cost': annual_pump_cost,
            'net_annual_savings': net_annual_savings,
            'simple_payback_years': simple_payback,
            'npv_10yr': npv_10yr,
            'cost_per_kwh_delivered': self.specs.capital_cost / (annual_energy * self.specs.lifetime_years)
        }

# ============================================================================
# COMPARISON TO ALTERNATIVES
# ============================================================================

def compare_heating_systems(location_data: Dict) -> Dict:
    """
    Compare ITB-100 to alternative heating solutions
    
    Returns:
        Dictionary comparing capital cost, operating cost, carbon footprint
    """
    systems = {
        'ITB-100 + Solar Thermal': {
            'capital_cost': 3500 + 6000,  # Battery + solar collectors
            'annual_operating_cost': 75,  # Pump electricity only
            'lifetime': 10,  # years
            'carbon_kg_per_year': 100,  # Minimal (pump electricity)
        },
        'Natural Gas Furnace': {
            'capital_cost': 4000,
            'annual_operating_cost': 1200,  # Fuel cost (typical for Syracuse)
            'lifetime': 15,
            'carbon_kg_per_year': 3500,  # COâ‚‚ emissions
        },
        'Air Source Heat Pump': {
            'capital_cost': 8000,
            'annual_operating_cost': 900,
            'lifetime': 15,
            'carbon_kg_per_year': 1500,  # Grid electricity
        },
        'Electric Resistance': {
            'capital_cost': 1500,
            'annual_operating_cost': 2400,
            'lifetime': 20,
            'carbon_kg_per_year': 4000,
        }
    }
    
    # Calculate 10-year total cost of ownership
    for system, data in systems.items():
        years = min(10, data['lifetime'])
        data['total_cost_10yr'] = data['capital_cost'] + data['annual_operating_cost'] * years
        data['carbon_10yr_kg'] = data['carbon_kg_per_year'] * years
    
    return systems

# ============================================================================
# VISUALIZATION
# ============================================================================

def plot_discharge_performance(discharge_results: Dict, save_path: str = None):
    """Create comprehensive discharge performance plots"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('ITB-100 Discharge Performance', fontsize=16, fontweight='bold')
    
    # Plot 1: Power output over time
    ax1 = axes[0, 0]
    ax1.plot(discharge_results['time'], discharge_results['Q'], 'b-', linewidth=2)
    ax1.axhline(y=2.0, color='r', linestyle='--', label='Target (2.0 kW)')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Power Output (kW)')
    ax1.set_title('Power Output vs Time')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot 2: Temperature profiles
    ax2 = axes[0, 1]
    ax2.plot(discharge_results['time'], discharge_results['T_sat'], 'r-', linewidth=2, label='SAT Temperature')
    ax2.plot(discharge_results['time'], discharge_results['T_out'], 'b-', linewidth=2, label='Water Outlet')
    ax2.axhline(y=58.0, color='k', linestyle='--', alpha=0.5, label='Phase Change Temp')
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Temperature (Â°C)')
    ax2.set_title('Temperature Profiles')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Plot 3: State of charge
    ax3 = axes[1, 0]
    ax3.plot(discharge_results['time'], discharge_results['SOC'] * 100, 'g-', linewidth=2)
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('State of Charge (%)')
    ax3.set_title('State of Charge vs Time')
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim([0, 105])
    
    # Plot 4: Phase state
    ax4 = axes[1, 1]
    ax4.plot(discharge_results['time'], discharge_results['solid_fraction'] * 100, 'm-', linewidth=2)
    ax4.set_xlabel('Time (hours)')
    ax4.set_ylabel('Solid Fraction (%)')
    ax4.set_title('Crystallization Progress')
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim([0, 105])
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

def plot_charge_performance(charge_results: Dict, save_path: str = None):
    """Create comprehensive charge performance plots"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('ITB-100 Charge Performance (Solar Thermal)', fontsize=16, fontweight='bold')
    
    # Plot 1: Power absorption vs available
    ax1 = axes[0, 0]
    ax1.plot(charge_results['time'], charge_results['Q_available'], 'orange', 
             linewidth=2, alpha=0.5, label='Solar Available')
    ax1.plot(charge_results['time'], charge_results['Q'], 'b-', linewidth=2, label='Battery Absorbed')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Power (kW)')
    ax1.set_title('Charging Power vs Time')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot 2: Temperature profiles
    ax2 = axes[0, 1]
    ax2.plot(charge_results['time'], charge_results['T_sat'], 'r-', linewidth=2, label='SAT Temperature')
    ax2.axhline(y=58.0, color='k', linestyle='--', alpha=0.5, label='Phase Change Temp')
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Temperature (Â°C)')
    ax2.set_title('SAT Temperature During Charge')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Plot 3: State of charge
    ax3 = axes[1, 0]
    ax3.plot(charge_results['time'], charge_results['SOC'] * 100, 'g-', linewidth=2)
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('State of Charge (%)')
    ax3.set_title('State of Charge vs Time')
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim([0, 105])
    
    # Plot 4: Phase state
    ax4 = axes[1, 1]
    ax4.plot(charge_results['time'], (1 - charge_results['solid_fraction']) * 100, 
             'm-', linewidth=2)
    ax4.set_xlabel('Time (hours)')
    ax4.set_ylabel('Liquid Fraction (%)')
    ax4.set_title('Melting Progress')
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim([0, 105])
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

# ============================================================================
# MAIN ANALYSIS SCRIPT
# ============================================================================

def main(output_dir: str = './output'):
    """
    Run ITB-100 thermal battery system analysis
    
    Args:
        output_dir: Directory to save output files (default: ./output)
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("=" * 70)
    print("ITB-100 THERMAL BATTERY SYSTEM MODEL")
    print("=" * 70)
    print(f"\n⚠️  UNVALIDATED MODEL - For research purposes only")
    print(f"Output directory: {output_path.absolute()}\n")
    print("=" * 70)
    
    # Initialize system
    specs = ITB100Specs()
    
    # ========================================================================
    # 1. DISCHARGE SIMULATION
    # ========================================================================
    print("\n" + "=" * 70)
    print("DISCHARGE SIMULATION")
    print("=" * 70)
    
    discharge_results = simulate_discharge(specs, T_supply=40.0, dt=60.0)
    
    print(f"\nDischarge Performance:")
    print(f"  Duration: {discharge_results['duration']:.2f} hours")
    print(f"  Average Power: {discharge_results['avg_power']:.2f} kW")
    print(f"  Total Energy Delivered: {discharge_results['total_energy']:.2f} kWh")
    print(f"  Target Energy: {specs.E_storage:.2f} kWh")
    print(f"  Efficiency: {discharge_results['total_energy']/specs.E_storage*100:.1f}%")
    
    # ========================================================================
    # 2. CHARGE SIMULATION
    # ========================================================================
    print("\n" + "=" * 70)
    print("CHARGE SIMULATION (Solar Thermal)")
    print("=" * 70)
    
    # Generate solar profile for Syracuse, NY winter day
    time_solar, Q_solar, T_solar = generate_solar_profile(
        location="Syracuse_NY",
        collector_area=12.0,
        collector_efficiency=0.65
    )
    
    charge_results = simulate_charge(specs, Q_solar, T_solar, dt=60.0)
    
    print(f"\nCharge Performance:")
    print(f"  Duration: {charge_results['duration']:.2f} hours")
    print(f"  Average Power: {charge_results['avg_power']:.2f} kW")
    print(f"  Total Energy Stored: {charge_results['total_energy']:.2f} kWh")
    print(f"  Target Energy: {specs.E_storage:.2f} kWh")
    print(f"  Charge Efficiency: {charge_results['total_energy']/specs.E_storage*100:.1f}%")
    
    # ========================================================================
    # 3. ECONOMIC ANALYSIS
    # ========================================================================
    print("\n" + "=" * 70)
    print("ECONOMIC ANALYSIS (Syracuse, NY)")
    print("⚠️  Climate and economic data specific to Syracuse, NY")
    print("=" * 70)
    
    location_data = {
        'name': 'Syracuse, NY',
        'heating_degree_days': 6756,
        'avg_winter_temp': -2.0,  # °C
        # NOTE: For other locations, modify these parameters:
        # - heating_degree_days: Annual HDD for your location
        # - avg_winter_temp: Typical winter temperature
        # - Electric rates in EconomicModel class (line ~520)
    }
    
    economic = EconomicModel(specs, location_data)
    
    # Compare different baseline heating systems
    fuel_types = ['natural_gas', 'propane', 'electric_resistance', 'heat_pump']
    
    print("\nComparison vs Alternative Heating:")
    print("-" * 70)
    
    for fuel in fuel_types:
        economics = economic.calculate_annual_savings(cycles_per_year=150, heat_source=fuel)
        
        print(f"\n{fuel.replace('_', ' ').title()}:")
        print(f"  Annual Energy Delivered: {economics['annual_energy_delivered']:.0f} kWh")
        print(f"  Annual Fuel Savings: ${economics['annual_fuel_savings']:.2f}")
        print(f"  Annual Pump Cost: ${economics['annual_pump_cost']:.2f}")
        print(f"  Net Annual Savings: ${economics['net_annual_savings']:.2f}")
        print(f"  Simple Payback: {economics['simple_payback_years']:.1f} years")
        print(f"  10-Year NPV: ${economics['npv_10yr']:.2f}")
        print(f"  Levelized Cost: ${economics['cost_per_kwh_delivered']:.3f}/kWh")
    
    # ========================================================================
    # 4. SYSTEM COMPARISON
    # ========================================================================
    print("\n" + "=" * 70)
    print("HEATING SYSTEM COMPARISON")
    print("=" * 70)
    
    comparison = compare_heating_systems(location_data)
    
    print("\n10-Year Total Cost of Ownership:")
    print("-" * 70)
    for system, data in comparison.items():
        print(f"\n{system}:")
        print(f"  Capital Cost: ${data['capital_cost']:,.0f}")
        print(f"  10-Year Operating Cost: ${data['annual_operating_cost']*10:,.0f}")
        print(f"  Total 10-Year Cost: ${data['total_cost_10yr']:,.0f}")
        print(f"  10-Year Carbon Emissions: {data['carbon_10yr_kg']:,.0f} kg COâ‚‚")
    
    # ========================================================================
    # 5. GENERATE PLOTS
    # ========================================================================
    print("\n" + "=" * 70)
    print("GENERATING PERFORMANCE PLOTS")
    print("=" * 70)
    
    plot_discharge_performance(discharge_results, 
                               save_path=str(output_path / 'discharge_performance.png'))
    print("  âœ“ Discharge performance plot saved")
    
    plot_charge_performance(charge_results, 
                           save_path=str(output_path / 'charge_performance.png'))
    print("  âœ“ Charge performance plot saved")
    
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print(f"Results saved to: {output_path.absolute()}")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='ITB-100 Thermal Battery System Model',
        epilog='⚠️  This model is UNVALIDATED. For research purposes only.'
    )
    parser.add_argument('--output-dir', default='./output',
                       help='Directory for output files (default: ./output)')
    
    args = parser.parse_args()
    
    main(output_dir=args.output_dir)

