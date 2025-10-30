# ITB-100 Models & Analysis

Python models for analyzing the ITB-100 thermal battery system.

## ⚠️ Critical Disclaimer

**These models are UNVALIDATED**. No physical prototype has been built or tested. Real-world performance may differ significantly from predictions.

Use these models for:
- ✅ Research and conceptual design
- ✅ Understanding system behavior
- ✅ Comparing alternatives

Do NOT use for:
- ❌ Final engineering design
- ❌ Financial projections for funding
- ❌ Performance guarantees

## 📁 Files

| File | Purpose | Runtime |
|:-----|:--------|:-------:|
| `../models/itb100_system_model.py` | Core thermal dynamics model | ~30 sec |
| `../models/heat_pump_assist_analysis.py` | Shoulder season use case | ~15 sec |
| `../models/itb100_market_analysis.py` | Market sizing & economics | ~20 sec |
| `../models/thermal_vs_lithium_comparison.py` | Cost comparison with batteries | ~15 sec |
| `../requirements.txt` | Python dependencies | - |

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running Models

```bash
# Run all models from project root
python models/itb100_system_model.py
python models/heat_pump_assist_analysis.py
python models/itb100_market_analysis.py
python models/thermal_vs_lithium_comparison.py

# Or from models/ directory
cd models/
python itb100_system_model.py --output-dir ../output

# Get help
python models/itb100_system_model.py --help
```

### Output Files

All models save results to `./output/` directory (or custom path):

**System Model:**
- `discharge_performance.png` - Power output over time
- `charge_performance.png` - Solar charging profile

**Heat Pump Analysis:**
- `heat_pump_assist_analysis.png` - Shoulder season economics

**Market Analysis:**
- `itb100_market_analysis.png` - Market sizing & competitive landscape

## 📊 Model Details

### 1. itb100_system_model.py

**Purpose:** Physics-based model of charge/discharge thermal dynamics

**Key Outputs:**
- Discharge duration: 9.30 hours
- Average power: 1.68 kW
- Energy delivered: 15.68 kWh (93.9% of capacity)
- Round-trip efficiency: 90-95%

**Key Assumptions:**
- SAT phase change at 58°C
- UA value: 111.7 W/K (UNVALIDATED)
- 1,000+ cycle life (literature-based, NOT tested)
- Syracuse, NY climate (modify `location_data` dict for your area)

**Modify for your location:**
- Line 833: `location_data` dictionary
- Line 755: Solar profile parameters

---

### 2. heat_pump_assist_analysis.py

**Purpose:** Analyze dual-fuel heat pump + thermal storage in shoulder seasons

**Use Case:**
- Heat pump + furnace backup system
- Balance point: 35°F
- Shoulder season operation (Mar-May, Sep-Nov)
- Syracuse, NY climate

**Key Results:**
- Annual cycles: 139 days
- Electric avoided: 730 kWh/year
- Savings: $339/year (with 30% ITC)
- Payback: 22.7 years

**Key Assumptions:**
- Electric rate: $0.18/kWh peak (line 285)
- Heat pump COP curve (lines 23-47)
- Solar availability (line 63-80)
- Equipment life value: $141/year (line 272)

**Modify for your system:**
- Line 63: `ShoulderSeasonConditions` class
- Line 266: Economic assumptions (rates, carbon price)

---

### 3. itb100_market_analysis.py

**Purpose:** Market sizing, competitive analysis, and pricing scenarios

**Key Results:**
- 2030 TAM: 1,375,000 units
- Realistic market (25% penetration): 344,000 units
- Target price: $4,500 installed
- Manufacturing cost at 1,000 units: $1,500 (ESTIMATE)

**⚠️ Critical Warnings:**
- **Market projections are UNVALIDATED**
- Data as of October 2025 (will become stale)
- Competitor pricing will change
- Manufacturing costs are estimates, NOT quotes

**Key Assumptions:**
- 15% annual heat pump growth
- 25% thermal storage penetration by 2030
- Gas bans in 8+ states
- Cost scaling based on analogous products

---

## 🔧 Modifying Models

### Change Location (System Model & Heat Pump Analysis)

Edit location data in each file:

**itb100_system_model.py (line ~833):**
```python
location_data = {
    'name': 'Your City, State',
    'heating_degree_days': 5000,  # Your HDD
    'avg_winter_temp': 0.0         # °C
}
```

**heat_pump_assist_analysis.py (line ~63):**
```python
@dataclass
class ShoulderSeasonConditions:
    spring_avg_temp_F: float = 45.0  # Your spring temp
    fall_avg_temp_F: float = 50.0     # Your fall temp
    # ... etc
```

### Change Economic Assumptions

**Electric rates (heat_pump_assist_analysis.py, line ~285):**
```python
electric_rate = 0.18  # Change to your peak rate ($/kWh)
```

**Carbon pricing (line ~276):**
```python
carbon_value = (carbon_avoided_kg / 1000) * 50  # Change 50 to your $/ton
```

### Add Uncertainty Analysis

Models currently show single-point estimates. To add uncertainty:

1. Define parameter ranges
2. Run Monte Carlo simulations
3. Plot probability distributions

Example:
```python
# Add to any model
import numpy as np

n_simulations = 1000
results = []

for i in range(n_simulations):
    # Vary key parameters
    UA_value = np.random.normal(111.7, 15)  # ±15 W/K uncertainty
    electric_rate = np.random.uniform(0.12, 0.20)
    
    # Run model with varied parameters
    result = run_model(UA_value, electric_rate)
    results.append(result)

# Analyze distribution
mean_payback = np.mean([r['payback'] for r in results])
percentile_90 = np.percentile([r['payback'] for r in results], 90)
```

## 📚 Understanding the Models

### Model Validation Status

| Component | Validation Level | Evidence |
|:----------|:-----------------|:---------|
| **SAT Chemistry** | Literature ⚠️ | 30+ years research, NOT tested in ITB-100 |
| **Heat Transfer** | Calculated ⚠️ | Based on thermal resistance equations |
| **Solar Charging** | Modeled ⚠️ | Evacuated tube performance curves |
| **Economics** | Estimated ⚠️ | Based on analogous products |
| **Market Size** | Projected ⚠️ | Industry analyst reports |

**Key:** ❌ No validation | ⚠️ Theoretical only | ✅ Experimentally validated

### Sources of Uncertainty

**High Uncertainty (±50%+):**
- Manufacturing cost at volume (no quotes)
- Market penetration rate (optimistic?)
- Equipment life extension value

**Medium Uncertainty (±20-30%):**
- Heat transfer coefficient (UA value)
- Solar charging efficiency (weather-dependent)
- Economic value assumptions

**Low Uncertainty (±10%):**
- SAT latent heat (well-established)
- Basic thermal dynamics
- Energy storage capacity

### Sensitivity Analysis

Most sensitive parameters (change output by >20%):

1. **Electric rate** (heat pump analysis)
   - +$0.05/kWh → Improves payback by ~5 years

2. **Manufacturing cost** (all models)
   - +50% → Increases payback by ~10 years

3. **Cycle life** (all models)
   - -50% cycles → Doubles levelized cost

4. **Heat transfer coefficient** (system model)
   - -20% UA → Reduces power output by ~20%

---

## 🐛 Known Issues & Limitations

### Current Limitations

1. **No uncertainty quantification**
   - All outputs are point estimates
   - No confidence intervals

2. **Location-specific**
   - Hardcoded for Syracuse, NY
   - Requires manual editing for other locations

3. **No time-series simulation**
   - Single-cycle analysis only
   - Doesn't model year-long operation

4. **Simplified economics**
   - Doesn't account for:
     - Electric rate escalation
     - Discount rates
     - Inflation
     - Tax implications (beyond ITC)

5. **No degradation modeling**
   - Assumes constant performance over 10 years
   - Real systems degrade over time

### Planned Improvements

See [COMPLETION_CHECKLIST.md](COMPLETION_CHECKLIST.md) for planned enhancements:

- [ ] Add command-line location selection
- [ ] Monte Carlo uncertainty analysis
- [ ] Time-series simulation (hourly, annual)
- [ ] Degradation models
- [ ] Unit tests
- [ ] Jupyter notebook tutorials

---

## 🤝 Contributing

Found an issue? Want to improve the models?

1. **Report bugs:** Open a GitHub Issue
2. **Suggest improvements:** Submit a Pull Request
3. **Share validation data:** If you build a prototype, share performance data!

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📖 Further Reading

**Phase Change Materials:**
- Mehling & Cabeza: "Heat and Cold Storage with PCM" (textbook)
- Sharma et al. (2009): "Review on thermal energy storage with PCM"

**SAT Thermal Storage:**
- Dannemand et al. (2016): "Long-term thermal stability of SAT"
- Wada et al. (2003): "SAT as phase change material"

**Building Electrification:**
- NREL: "Electrification Futures Study" (2023)
- NYSERDA: "Gas Ban Impact Analysis" (2024)

---

## 📞 Questions?

- **Model usage:** Open a GitHub Issue
- **Collaboration:** See [README.md](../README.md) for contact info
- **Commercial interest:** Contact project maintainer

---

*Last updated: October 30, 2025*  
*Model version: 1.0 (unvalidated)*
