# Benchtop Validation Test - Detailed Protocol

**Purpose:** Validate ITB-100 thermal battery core assumptions before building $9,500 full system  
**Cost:** $250 (materials + instrumentation)  
**Time:** 1 week build + 4 weeks testing  
**Success Criteria:** >95% nucleation reliability, ±20% power output accuracy, <5% capacity degradation

---

## ðŸ›  **Bill of Materials (with part numbers)**

### **Structural Components**

| Item | Spec | Qty | Supplier | Part # | Cost |
|:-----|:-----|:---:|:---------|:-------|-----:|
| Aluminum plate | 300×400×2mm (6061-T6) | 1 | OnlineMetals | AL-6061-T6-SHEET-2MM | $25 |
| SS316L tubing | 3/4" OD, 0.035" wall | 0.5 m | McMaster-Carr | 8988K211 | $15 |
| Thermal epoxy | Arctic Alumina Adhesive | 1 tube | Amazon | B0087X728K | $20 |
| LDPE sheet | 0.004" thick, clear | 1 m² | USPlastic | 40065 | $15 |
| Heat seal tape | 1/2" width | 1 roll | Amazon | B07QXZXN2K | $8 |

### **Phase Change Material & Additives**

| Item | Spec | Qty | Supplier | Part # | Cost |
|:-----|:-----|:---:|:---------|:-------|-----:|
| Sodium acetate trihydrate | ACS grade, ≥99% | 5 kg | LabAlley | 7132-SAT-5KG | $40 |
| Sodium polyacrylate | (Na-PMAA), MW ~5000 | 50 g | Sigma-Aldrich | 416010-50G | $20 |
| Disodium phosphate | (Na₂HPO₄), anhydrous | 100 g | Fisher Scientific | S374-100 | $5 |

### **Nucleation System**

| Item | Spec | Qty | Supplier | Part # | Cost |
|:-----|:-----|:---:|:---------|:-------|-----:|
| Silver wire | 22 AWG, 99.9% pure | 1 m | Amazon | B07KWXP8YQ | $5 |
| Power supply | 0-5V DC, 1A | 1 | Amazon | B07MW3KKCX | $12 |
| Relay module | 5V, optoisolated | 1 | Amazon | B0057OC6D8 | $8 |

### **Instrumentation**

| Item | Spec | Qty | Supplier | Part # | Cost |
|:-----|:-----|:---:|:---------|:-------|-----:|
| K-type thermocouples | 1/16" probe, -50 to 200°C | 5 | Amazon | B07MBPC1BN | $25 |
| Thermocouple amplifier | MAX31855 breakout | 5 | Adafruit | 269 | $30 |
| Flow meter | 1/2" NPT, 0.5-10 GPM | 1 | Amazon | B07KRX8YX4 | $30 |
| Arduino Mega | 2560 R3 | 1 | Amazon | B01H4ZLZLQ | $20 |
| SD card shield | Data logging | 1 | Adafruit | 1141 | $15 |
| Power meter | Kill-A-Watt style | 1 | Amazon | B00009MDBU | $25 |

### **Plumbing & Heating**

| Item | Spec | Qty | Supplier | Part # | Cost |
|:-----|:-----|:---:|:---------|:-------|-----:|
| Circulator pump | 1/40 HP, 1/2" NPT | 1 | Amazon | B00HWUJPCS | $45 |
| Immersion heater | 1500W, 120V | 1 | Amazon | B000BQVSHQ | $25 |
| PVC container | 5 gallon bucket | 2 | Home Depot | 05GLPAIL | $10 |
| Pipe fittings | 1/2" NPT assortment | 1 set | Home Depot | Various | $15 |

**TOTAL: ~$413** (can reduce to $250 if you have pump, heater, power supply)

---

## ðŸ"§ **Build Instructions**

### **Step 1: Prepare Aluminum Plate (1 hour)**

1. **Cut aluminum plate to size:** 300 × 400 mm (if not pre-cut)
2. **Drill tubing holes:**
   - Mark serpentine pattern (6 passes, 50mm spacing)
   - Drill 3/4" holes at ends for tubing entry/exit
   - Deburr all holes

3. **Surface preparation:**
   - Sand both sides with 220-grit sandpaper
   - Clean with isopropyl alcohol
   - Dry completely

### **Step 2: Install Tubing & Thermal Interface (2 hours)**

1. **Bend SS tubing:**
   - Create serpentine pattern across plate
   - Use tubing bender (or carefully by hand)
   - Ensure good thermal contact with plate surface

2. **Apply thermal epoxy:**
   - Mix Arctic Alumina per instructions
   - Apply thin, even layer (1-2mm) along tubing contact line
   - Press tubing firmly into epoxy
   - Clamp or weight down for 24 hours

3. **Cure:**
   - Let epoxy cure 24 hours at room temperature
   - DO NOT DISTURB during cure

### **Step 3: Prepare SAT Mixture (1 hour)**

⚠️ **SAFETY:** Wear gloves and safety glasses. Work in ventilated area.

1. **Calculate quantities:**
   - Target: 4.5 kg SAT
   - Na-PMAA: 0.67% = 30 g
   - Na₂HPO₄: 2.02% = 91 g

2. **Mixing procedure:**
   ```
   a) Heat 500 mL distilled water to 60°C in stainless steel pot
   b) Add 91g Na₂HPO₄, stir until dissolved
   c) Add 30g Na-PMAA slowly while stirring (prevents clumping)
   d) Add 4.5 kg sodium acetate trihydrate
   e) Heat to 70°C, stir until completely dissolved
   f) Check pH (should be 6-7, adjust if needed)
   ```

3. **Quality check:**
   - Solution should be clear, slightly viscous
   - No undissolved particles
   - pH 6-7 (use pH test strips)

### **Step 4: Create SAT Pouch (30 minutes)**

1. **Cut LDPE sheet:**
   - Two pieces: 350 × 450 mm each

2. **Seal three sides:**
   - Use heat sealer or iron (medium heat)
   - Create 10mm seal on three sides
   - Test seal strength by pulling

3. **Fill with SAT:**
   - Pour liquid SAT mixture into pouch while still hot (70°C)
   - Leave 50mm air space at top
   - Expel air bubbles by gently squeezing

4. **Seal fourth side:**
   - Ensure no air pockets remain
   - Create strong 10mm seal
   - Double-seal for safety

5. **Leak test:**
   - Inspect all seals visually
   - Gently squeeze - should hold pressure
   - If leak detected, reinforce or remake

### **Step 5: Install Nucleation System (30 minutes)**

1. **Prepare silver wire:**
   - Cut two pieces: 100mm each
   - Strip 10mm of insulation from ends
   - Clean with isopropyl alcohol

2. **Insert into pouch:**
   - BEFORE sealing fourth side, insert silver wires
   - Position 50mm apart in center of pouch
   - Ensure wires don't touch each other
   - Seal fourth side with wires exiting

3. **Wire to relay:**
   - Connect wires to relay module
   - Relay controlled by Arduino
   - Set to apply 1.5V DC for 30 seconds when triggered

### **Step 6: Assemble Test Rig (2 hours)**

1. **Hydraulic loop:**
   ```
   [Hot water bucket] → [Pump] → [Flow meter] → [Test cell] → [Return bucket]
   ```

2. **Mount test cell:**
   - Sandwich SAT pouch between aluminum plate and insulation
   - Apply even pressure (use clamps or weight)
   - Ensure good thermal contact

3. **Instrumentation:**
   - **TC1:** SAT center (inserted through small hole in pouch)
   - **TC2:** SAT top edge
   - **TC3:** SAT bottom edge  
   - **TC4:** Water inlet
   - **TC5:** Water outlet
   - **Flow meter:** In supply line
   - **Power meter:** On pump + heater

4. **Data logging:**
   - Connect all sensors to Arduino
   - Program to log every 60 seconds
   - Save to SD card as CSV

### **Step 7: Initial Checkout (1 hour)**

1. **Leak test:**
   - Fill system with water
   - Run pump for 10 minutes
   - Check all connections for leaks

2. **Sensor verification:**
   - Verify all 5 thermocouples read room temperature
   - Verify flow meter reads 0 when pump off
   - Verify data logging to SD card

3. **First heating test:**
   - Heat water to 65°C
   - Flow through system
   - Verify SAT melts (should take 1-2 hours)
   - Record all temperatures

---

## ðŸ§ª **Test Protocol (50-100 cycles)**

### **Cycle Structure (4-6 hours per cycle)**

Each cycle consists of:
1. **Charge Phase** (1-2 hours)
2. **Cooldown** (1-2 hours)
3. **Nucleation** (1 minute)
4. **Discharge Phase** (2-3 hours)

### **Detailed Procedure**

#### **CHARGE PHASE**

1. **Heat water to 70°C** in hot bucket (use immersion heater)
2. **Start pump** (set flow rate: 4.4 L/min = 1.16 GPM)
3. **Monitor temperatures:**
   - SAT should rise from ambient to 58°C (melting begins)
   - Continue until SAT reaches 65°C (fully liquid)
4. **Record:**
   - Time to complete melting
   - Total energy input (integrate power × time)
   - Temperature profiles (all 5 sensors)
5. **Stop when:** SAT reaches 65°C uniformly

#### **COOLDOWN PHASE**

1. **Turn off pump**
2. **Let SAT cool naturally** (or use cold water flow)
3. **Monitor for spontaneous nucleation:**
   - SAT should supercool below 58°C
   - Ideally reaches 20-30°C without crystallizing
4. **Record:**
   - Lowest temperature reached (degree of supercooling)
   - Any spontaneous crystallization events
5. **Stop when:** SAT reaches target temperature (20-30°C)

#### **NUCLEATION PHASE**

1. **Apply 1.5V to silver wire electrodes** via relay
2. **Hold for 30 seconds**
3. **Monitor for crystallization:**
   - Temperature should spike as latent heat releases
   - Should see ~28°C increase (58°C - 30°C = 28°C latent heat)
4. **Record:**
   - Nucleation success (yes/no)
   - Time from voltage application to crystallization start
   - Temperature spike magnitude
5. **If nucleation fails:**
   - Try again at lower temperature
   - Try mechanical shock (tap pouch)
   - Record as failure if still no nucleation after 3 attempts

#### **DISCHARGE PHASE**

1. **Heat water to 40°C** in supply bucket
2. **Start pump** (same flow rate: 4.4 L/min)
3. **Monitor temperatures:**
   - Water outlet should be warmer than inlet
   - SAT should stay at ~58°C during solidification
   - Outlet temp decreases as SAT fully solidifies
4. **Calculate power output:**
   ```
   Q(t) = m_dot × Cp × (T_out - T_in)
   
   Where:
   m_dot = 0.074 kg/s (mass flow rate)
   Cp = 4186 J/(kg·K) (water specific heat)
   T_out = measured outlet temp (°C)
   T_in = measured inlet temp (°C)
   ```
5. **Record:**
   - Power output vs time (every 60 seconds)
   - Total energy delivered (integrate Q over time)
   - Duration until power drops to <100W
6. **Stop when:** Power output drops below 100W (SAT fully solid)

### **Data to Collect**

For each cycle, log:

```csv
Cycle, Time_Charge(min), Time_Discharge(min), Energy_In(kWh), Energy_Out(kWh), 
Nucleation_Success(bool), Supercool_Temp(C), Peak_Power(W), Avg_Power(W),
TC1_SAT_Center(C), TC2_SAT_Top(C), TC3_SAT_Bottom(C), TC4_Water_In(C), TC5_Water_Out(C),
Flow_Rate(L/min), Notes(text)
```

### **Special Tests (Every 25 Cycles)**

1. **DSC Analysis:**
   - Extract 10g sample of SAT from pouch
   - Send to lab for Differential Scanning Calorimetry
   - Measure actual latent heat of fusion
   - Compare to initial value (264.4 kJ/kg)
   - **Acceptance:** <5% degradation

2. **Visual Inspection:**
   - Remove from test rig
   - Check for leaks, cracks, delamination
   - Check pouch seal integrity
   - Weigh pouch (detect slow leaks)
   - **Acceptance:** No leaks, <1% mass loss

3. **pH Check:**
   - Extract small sample
   - Measure pH
   - **Acceptance:** pH stays 6-7 (no corrosion)

---

## 📊 **Data Analysis**

### **Key Metrics to Calculate**

#### **1. Nucleation Reliability**

```python
nucleation_success_rate = (successes / total_attempts) × 100%

Target: >95%
Acceptable: >90%
Failure: <90%
```

#### **2. Power Output Accuracy**

```python
model_prediction = 1.68 kW (average discharge power)

actual_avg_power = mean(measured_power_output)
error = abs(actual_avg_power - model_prediction) / model_prediction × 100%

Target: <10% error
Acceptable: <20% error
Failure: >30% error
```

#### **3. UA Value (Heat Transfer Coefficient)**

```python
# During discharge phase, calculate UA from data:

Q_actual = m_dot × Cp × (T_out - T_in)  # W
LMTD = ((T_SAT - T_in) - (T_SAT - T_out)) / ln((T_SAT - T_in)/(T_SAT - T_out))

UA_measured = Q_actual / LMTD  # W/K

Model prediction: UA = 111.7 W/K (for full system)
For single cell: UA_cell = 111.7 / 52 = 2.15 W/K

Compare measured to predicted.
```

#### **4. Capacity Retention**

```python
initial_capacity = energy_delivered_cycle_1  # kWh
final_capacity = energy_delivered_cycle_100  # kWh

degradation = (initial_capacity - final_capacity) / initial_capacity × 100%

Target: <2% degradation
Acceptable: <5% degradation
Failure: >10% degradation
```

#### **5. Charge/Discharge Efficiency**

```python
efficiency = energy_delivered / energy_input × 100%

Target: >90%
Acceptable: >85%
Failure: <80%
```

---

## ✅ **Success Criteria Summary**

| Metric | Target | Acceptable | Failure |
|:-------|:------:|:----------:|:-------:|
| **Nucleation reliability** | 100% | >95% | <90% |
| **Power output error** | <10% | <20% | >30% |
| **Capacity degradation** | <2% | <5% | >10% |
| **Pouch leaks** | 0 | 0 | Any |
| **Efficiency** | >90% | >85% | <80% |

**Overall decision:**
- **PASS:** All metrics in Target or Acceptable range → Proceed to full system
- **FAIL:** Any metric in Failure range → Redesign or abandon

---

## ðŸš© **Red Flags to Watch For**

### **Immediate Stop Conditions**

1. **Pouch leak:** Stop immediately, fix or rebuild
2. **Spontaneous crystallization:** SAT crystallizes before nucleation applied
3. **No nucleation:** Can't trigger crystallization even after 3 attempts
4. **Thermal runaway:** Temperature exceeds 80°C (safety limit)

### **Concerning Trends**

1. **Nucleation success rate declining:** <95% in last 10 cycles
2. **Power output degrading:** >5% drop from initial cycles
3. **Increasing supercooling:** Harder to keep liquid as cycles progress
4. **pH drift:** Moving outside 6-7 range (indicates decomposition)

---

## 📝 **Reporting Results**

At end of 50-100 cycles, prepare report with:

1. **Summary Statistics:**
   - Nucleation success rate
   - Average power output
   - Capacity degradation
   - Efficiency

2. **Comparison to Model:**
   - Predicted vs actual power output
   - Predicted vs measured UA value
   - Predicted vs actual efficiency

3. **Graphs:**
   - Power output vs time (typical cycle)
   - Temperature profiles (typical cycle)
   - Capacity over cycles (degradation trend)
   - Nucleation success rate over cycles

4. **Recommendations:**
   - GO decision: Confidence in full system build
   - NO-GO decision: Identified failure modes
   - ITERATE decision: Needed design changes

---

## ðŸ'¡ **Tips for Success**

1. **Start with 10 "shake-down" cycles** to debug instrumentation and procedure
2. **Take detailed notes** on every cycle - patterns emerge
3. **Use a spreadsheet** for real-time data entry (not just data logger)
4. **Video record** key events (nucleation, melting) for documentation
5. **Be patient** - each cycle takes 4-6 hours, can only run 1-2 per day
6. **Maintain consistency** - same flow rate, same temperatures each cycle
7. **Plan for failures** - expect 5-10% of cycles to have issues

---

## â± **Timeline**

**Week 1:** Build (2-3 days) + Initial checkout (1-2 days)  
**Week 2:** Cycles 1-10 (shake-down)  
**Week 3:** Cycles 11-30  
**Week 4:** Cycles 31-50  
**Week 5 (optional):** Cycles 51-100 for higher confidence  
**Week 6:** Data analysis + report writing

**Minimum viable test:** 50 cycles  
**High confidence test:** 100 cycles

---

## 🎯 **What This Test Proves**

### **If Successful:**

✅ **Nucleation system works** (can reliably trigger crystallization)  
✅ **Power output is predictable** (model accuracy within 20%)  
✅ **SAT is stable** (no significant degradation over 100 cycles)  
✅ **Heat transfer is adequate** (UA value matches predictions)  
✅ **Pouch construction works** (survives thermal cycling)

**Confidence to proceed:** HIGH (95%+)

### **If Partially Successful:**

⚠️ **Some metrics pass, others marginal:**
- Nucleation works but power output is low → Improve heat transfer
- Power is good but nucleation unreliable → Try different electrodes/stabilizers
- Everything works but efficiency is low → Reduce thermal losses

**Confidence to proceed:** MEDIUM (60-80%)  
**Action:** Iterate design based on learnings

### **If Unsuccessful:**

❌ **Critical failures identified:**
- Nucleation doesn't work (<90% success rate)
- Power output way off (>30% error)
- Rapid degradation (>10% capacity loss)

**Confidence to proceed:** LOW (<50%)  
**Action:** Major redesign or abandon

---

**Good luck! This test will definitively answer whether the ITB-100 design is viable before you commit to the full $9,500 system.**

*Protocol version 1.0 - October 30, 2025*
