# Validation Test Protocol: Single-Cell SAT Module

**Purpose:** Validate core ITB-100 thermal storage concept before building full system

**Scale:** 1/50th of full design  
**Cost:** ~$180 in materials  
**Time:** 3 days build + 4 weeks testing  
**Goal:** Answer critical questions about SAT chemistry, nucleation, and thermal performance

---

## 🎯 What This Test Will Tell You

### Critical Questions

✅ **Phase Change Chemistry:**
1. Does SAT with stabilizers cycle reliably 50+ times?
2. What's the real supercooling duration? (24 hours? 48 hours?)
3. Does phase separation occur after repeated cycling?
4. Any unexpected crystallization behavior?

✅ **Nucleation System:**
5. Does 1.5V silver electrode trigger work reliably?
6. What's the success rate? (Target: >95%)
7. How long does nucleation take after trigger? (Should be <5 minutes)
8. Any auto-nucleation events (unwanted crystallization)?

✅ **Thermal Performance:**
9. What's the measured UA value (thermal conductance)?
10. Does power output match the model predictions?
11. How uniform is the temperature in the SAT?
12. What's the charge/discharge efficiency?

✅ **Mechanical Durability:**
13. Does the HDPE pouch survive 50 thermal cycles?
14. Any aluminum corrosion or thermal epoxy degradation?
15. Does the system hold pressure over time?

---

## 🔧 Bill of Materials

| Item | Specification | Quantity | Unit Cost | Total | Source |
|:-----|:--------------|:--------:|:---------:|:-----:|:-------|
| **Phase Change Material** |
| Sodium acetate trihydrate | CH₃COONa·3H₂O, 99%+ | 4.5 kg | $8/kg | $36 | Chemical supplier |
| Sodium polymethacrylate | Na-PMAA, MW 15,000 | 30 g | $2/g | $6 | Polymer supplier |
| Disodium hydrogen phosphate | Na₂HPO₄, anhydrous | 91 g | $0.20/g | $18 | Chemical supplier |
| **Heat Exchanger** |
| Aluminum plate | 6061-T6, 300×400×2mm | 1 pc | $15 | $15 | Metal supplier |
| SS tubing | 316L, 1/2" OD, 0.035" wall | 0.5 m | $4/m | $2 | McMaster-Carr |
| Thermal epoxy | Arctic Silver or equivalent | 50 g | $12 | $12 | Electronics supplier |
| **Pouch & Sealing** |
| HDPE sheet | 0.5mm thick | 350×450mm | $5 | $5 | Plastic supplier |
| Impulse sealer | Heat sealer for HDPE | 1 pc | $25 | $25 | Amazon |
| **Nucleation System** |
| Silver wire | 99.9%, 1mm diameter | 0.2 m | $2/m | $1 | Jewelry supply |
| DC power supply | 0-5V adjustable | 1 pc | $15 | $15 | Amazon |
| **Instrumentation** |
| K-type thermocouples | ±0.5°C accuracy | 5 pc | $3 | $15 | Amazon |
| Arduino Uno | For data logging | 1 pc | $25 | $25 | Arduino store |
| SD card shield | For logging | 1 pc | $10 | $10 | Amazon |
| SD card | 8GB minimum | 1 pc | $8 | $8 | Amazon |
| **Heating/Cooling** |
| Hot plate | With temperature control | 1 pc | $40 | Use existing |
| Ice bath container | Large enough for module | 1 pc | $0 | Use existing |
| Circulating pump | Small aquarium pump | 1 pc | $15 | $15 | Pet store |
| **Miscellaneous** |
| Silicone tubing | 1/2" ID for water flow | 2 m | $2/m | $4 | Hardware store |
| Insulation | Foam board scraps | -- | $0 | Use existing |
| **TOTAL** |  |  |  | **~$180** |  |

---

## 🏗️ Construction Steps

### Step 1: Prepare SAT Mixture (2 hours)

**Safety first:** Wear gloves and eye protection. Work in ventilated area.

1. **Calculate masses:**
   ```
   SAT (pure):           4,370 g  (97.1%)
   Na-PMAA (stabilizer):    30 g  ( 0.67%)
   Na₂HPO₄ (stabilizer):    91 g  ( 2.02%)
   ────────────────────────────────
   Total:                4,491 g  (100%)
   ```

2. **Mixing procedure:**
   - Heat distilled water to 60°C in a large beaker
   - Slowly add SAT crystals, stirring until dissolved
   - Add Na-PMAA powder, stir for 10 minutes until fully dissolved
   - Add Na₂HPO₄, stir for 10 minutes
   - Continue heating and stirring for 30 minutes to ensure homogeneity
   - Visually inspect: Should be clear liquid (no cloudiness)

3. **Cool to room temperature** (naturally, don't rush)

### Step 2: Fabricate Heat Exchanger Plate (3 hours)

1. **Mark tubing path** on aluminum plate:
   ```
   Serpentine pattern: 8 passes across 300mm width
   Spacing: 40mm between passes
   Entry/exit on same side
   ```

2. **Machine shallow groove** (optional, improves contact):
   - 10mm wide, 1mm deep along tubing path
   - Can use router or milling machine
   - Alternative: Use thermal epoxy without groove

3. **Bend stainless tubing:**
   - Create 180° bends at ends (use tube bender)
   - Test-fit on plate before bonding
   - Leave 50mm straight sections at inlet/outlet

4. **Bond tubing to plate:**
   - Clean both surfaces with isopropyl alcohol
   - Apply thermal epoxy to groove (or plate surface)
   - Press tubing firmly into epoxy
   - Use clamps or weights to maintain contact
   - Cure per epoxy instructions (typically 24 hours)

### Step 3: Fabricate Pouch (1 hour)

1. **Cut HDPE sheet:** 350×450mm rectangle

2. **Create pouch:**
   - Fold in half (175×450mm when folded)
   - Heat-seal three sides using impulse sealer
   - Leave one short side open for filling
   - Test seal by filling with water first!

3. **Install nucleation electrodes:**
   - Insert two silver wires through sealed edge
   - Position 50mm apart in center of pouch
   - Seal around wires with additional HDPE patch
   - Connect wires to power supply (outside of pouch)

### Step 4: Assemble Module (30 minutes)

1. **Fill pouch with SAT mixture:**
   - Use funnel to pour prepared SAT solution
   - Fill to 90% capacity (allow for expansion)
   - Squeeze out air bubbles gently
   - Heat-seal final edge quickly (SAT must stay liquid)

2. **Bond pouch to heat exchanger:**
   - Apply thin layer of thermal epoxy to plate
   - Press pouch firmly against plate
   - Ensure good contact over entire surface
   - Allow to cure (24 hours)

3. **Insulate sides:**
   - Wrap exposed pouch edges with foam board
   - Leave heat exchanger side exposed
   - Goal: Force heat transfer through plate only

### Step 5: Install Instrumentation (2 hours)

1. **Attach thermocouples:**
   - TC1: Aluminum plate surface (center)
   - TC2: SAT bulk temperature (insert through sealed edge)
   - TC3: Water inlet temperature
   - TC4: Water outlet temperature
   - TC5: Ambient temperature

2. **Connect to Arduino:**
   ```cpp
   // Simple Arduino code for 5-channel thermocouple logging
   #include <SD.h>
   
   void setup() {
     Serial.begin(9600);
     SD.begin(chipSelect);
   }
   
   void loop() {
     // Read all 5 thermocouples
     float T1 = readTC(A0);  // Plate
     float T2 = readTC(A1);  // SAT
     float T3 = readTC(A2);  // Inlet
     float T4 = readTC(A3);  // Outlet
     float T5 = readTC(A4);  // Ambient
     
     // Log to SD card with timestamp
     logData(millis(), T1, T2, T3, T4, T5);
     
     delay(60000);  // Sample every 60 seconds
   }
   ```

3. **Test data logging:**
   - Verify all sensors reading correctly
   - Check SD card writes
   - Calibrate if needed (ice water = 0°C, boiling water = 100°C)

---

## 🧪 Testing Protocol (4 Weeks)

### Week 1: Baseline Characterization

**Goal:** Establish initial performance before cycling

1. **DSC Measurement (if available):**
   - Take 10mg sample of SAT mixture
   - Measure latent heat of fusion
   - Target: 264 kJ/kg
   - Document: Take photo of DSC curve

2. **Initial Melt-Freeze Cycle:**
   - Heat to 65°C (clear liquid)
   - Cool to 25°C (trigger nucleation)
   - Measure: Time to complete crystallization
   - Expected: <10 minutes once triggered

3. **UA Value Measurement:**
   - Circulate 40°C water through tubing (constant flow)
   - Wait for steady-state (inlet = outlet temperature)
   - Measure SAT temperature vs. water temperature
   - Calculate: UA = Q / (T_water - T_SAT)
   - Expected: ~2.2 W/K for single cell

4. **Document Initial State:**
   - Photos of pouch (any bubbles? clarity?)
   - Dimensions (any swelling?)
   - Visual SAT appearance (color, clarity)

### Week 2-3: Accelerated Cycling (50 Cycles)

**Goal:** 50 charge/discharge cycles in 14 days

**Daily procedure (3-4 cycles/day):**

```
CYCLE SEQUENCE (repeats every 6 hours):

Hour 0:00 - CHARGE PHASE (Heating)
  - Set hot plate to 65°C
  - Monitor SAT temperature rise
  - Target: Complete melting (SAT = 60-65°C)
  - Log: Time to full melt, temperature profile
  
Hour 0:30 - SUPERCOOL PHASE (Cooling)
  - Transfer to ice bath (or turn off heat)
  - Cool to 25°C
  - Monitor: Does auto-nucleation occur? (it shouldn't)
  - Log: Supercooling duration

Hour 1:00 - NUCLEATION TRIGGER
  - Apply 1.5V DC across silver electrodes for 10 seconds
  - Observe: Temperature should spike to 58°C within 5 minutes
  - Log: Success/failure, time to crystallization
  
Hour 1:10 - DISCHARGE PHASE (Heat Extraction)
  - Circulate 40°C water through heat exchanger
  - Flow rate: ~0.1 L/min
  - Monitor outlet temperature vs. time
  - Continue until SAT = 40°C
  - Calculate: Energy delivered = ṁ × cp × ∫(T_out - T_in)dt
  
Hour 3:00 - REST PHASE
  - Allow system to equilibrate
  - Check for leaks, damage
  - Verify data logged correctly
  
Hour 6:00 - REPEAT
```

**Every 10 cycles:**
- Take detailed photos
- Measure pouch dimensions
- Re-measure UA value
- Visual inspection for degradation

### Week 4: Final Characterization

**Goal:** Compare performance after 50 cycles to baseline

1. **Final DSC Measurement:**
   - Take new 10mg sample
   - Compare latent heat: Should be >90% of initial
   - Document any change in melting temperature

2. **Final UA Measurement:**
   - Repeat steady-state test
   - Compare to Week 1 value
   - Acceptable: <10% degradation

3. **Destructive Inspection:**
   - Cut open pouch (carefully!)
   - Examine SAT visually: Any phase separation? Solid layers?
   - Inspect aluminum: Any corrosion?
   - Inspect thermal epoxy: Still bonded?

4. **Final Report:**
   - Summarize all data in spreadsheet
   - Create plots: Temperature profiles, power output over cycles
   - Document success rate: X/50 nucleation triggers successful
   - Note any anomalies or unexpected behavior

---

## 📊 Data Analysis

### Key Metrics to Calculate

1. **Nucleation Success Rate:**
   ```
   Success Rate = (Successful triggers / Total attempts) × 100%
   Target: ≥95%
   ```

2. **Capacity Retention:**
   ```
   Capacity = (Energy cycle 50 / Energy cycle 1) × 100%
   Target: >90%
   ```

3. **UA Value Stability:**
   ```
   UA Degradation = (UA_initial - UA_final) / UA_initial × 100%
   Target: <10%
   ```

4. **Average Discharge Power:**
   ```
   Power = ṁ × cp × (T_out_avg - T_in_avg)
   Expected: 30-40 W for single cell
   ```

5. **Round-Trip Efficiency:**
   ```
   Efficiency = (Energy out / Energy in) × 100%
   Target: >85%
   ```

### Plots to Generate

Using your data, create these plots:

1. **Temperature vs. Time (Cycle 1 vs. Cycle 50):**
   - Shows any degradation in thermal performance
   - Should overlay closely if no degradation

2. **Power Output vs. Cycle Number:**
   - Shows capacity fade over time
   - Should be relatively flat

3. **Nucleation Response (Temperature Spike):**
   - Shows how quickly crystallization starts
   - Should be <5 minutes consistently

4. **UA Value Over Time:**
   - Shows thermal interface degradation
   - Should be stable within 10%

---

## ✅ Success Criteria (Go/No-Go Decision)

Use this rubric to decide if full system is worth building:

| Metric | Target | Acceptable | FAIL |
|:-------|:------:|:----------:|:----:|
| **Nucleation success** | 100% (50/50) | ≥95% (48/50) | <90% |
| **Capacity retention** | >95% | >85% | <80% |
| **UA stability** | <5% change | <10% change | >15% |
| **Pouch integrity** | Perfect | Minor bulging | Any leaks |
| **Power output accuracy** | ±10% vs model | ±20% vs model | >30% off |
| **Auto-nucleation events** | 0 | ≤2 | >5 |

**Decision Matrix:**

✅ **All "Target" or "Acceptable"** → Full system is LOW RISK, proceed with confidence

⚠️ **Mix of "Acceptable" and one "Fail"** → MEDIUM RISK, consider design modifications before building full system

❌ **Multiple "Fail" criteria** → HIGH RISK, do not build full system without addressing issues

---

## 📝 Reporting Your Results

**What to share with the community:**

1. **Summary Report (GitHub Issue):**
   ```
   Title: "Single-cell validation test results - [GitHub username]"
   
   Content:
   - Test dates and duration
   - Key findings (3-5 bullet points)
   - Success criteria table (filled in)
   - Link to detailed data
   - Photos of module before/after
   - Lessons learned
   ```

2. **Data Files (GitHub PR to /data/):**
   ```
   /data/validation/[your-username]/
   ├── README.md           # Test conditions
   ├── cycle-001.csv       # All 50 cycle files
   ├── ...
   ├── cycle-050.csv
   ├── dsc-initial.pdf     # If available
   ├── dsc-final.pdf
   └── photos/             # Visual documentation
   ```

3. **Plots and Analysis:**
   - Generate the 4 key plots listed above
   - Include in your report
   - Share high-res versions

**Even if your test fails, please report it!** Negative results are just as valuable as positive ones. The community learns either way.

---

## 🚨 Safety Reminders

⚠️ **Chemical Handling:**
- SAT is low-toxicity but wear gloves
- Na-PMAA and Na₂HPO₄ are irritants - avoid skin contact
- Work in ventilated area
- Have eyewash station nearby

⚠️ **Thermal Hazards:**
- Hot plate can cause burns (65°C)
- Molten SAT at 60°C will burn skin
- Use tongs/gloves when handling heated components

⚠️ **Electrical:**
- 1.5V DC is safe, but avoid short circuits
- Keep water away from power supply
- Use GFCI outlet if near water

⚠️ **Pressure:**
- Pouch may swell during heating
- Do not overfill (90% max)
- Ensure seals are strong before heating

---

## ❓ FAQ

**Q: Can I use a different PCM instead of SAT?**  
A: Yes, but you'll need different stabilizers and nucleation method. SAT is chosen for its 58°C phase change temp (ideal for heating) and proven chemistry.

**Q: What if my nucleation success rate is <95%?**  
A: Try increasing voltage (up to 3V), increasing electrode surface area, or improving electrode contact with SAT. If still failing, may need different electrode material (copper, zinc).

**Q: My UA value is lower than expected. Why?**  
A: Likely thermal interface issue. Check: (1) Thermal epoxy bond quality, (2) Air gaps between plate and pouch, (3) SAT mixture homogeneity.

**Q: Can I speed up the testing (more cycles/day)?**  
A: Yes, but ensure complete melting and crystallization each cycle. Rushing can lead to incomplete phase change and skewed results.

**Q: Should I cycle continuously or take breaks?**  
A: Continuous cycling is fine. The 3-hour rest in the protocol is for data checking, not required for SAT chemistry.

**Q: What if SAT auto-nucleates (crystallizes without trigger)?**  
A: This indicates insufficient stabilizer or contamination. Try: (1) Remix with fresh chemicals, (2) Increase Na-PMAA concentration slightly, (3) Ensure pouch is clean.

---

## 🎯 Next Steps After Validation

**If your test succeeds (≥90% on all metrics):**

1. **Share your results** publicly (GitHub, YouTube, blog post)
2. **Consider building full system** with confidence
3. **Help others** by answering questions
4. **Contribute improvements** to the design

**If your test fails:**

1. **Share your results** (equally important!)
2. **Identify root cause** (chemistry? thermal? mechanical?)
3. **Propose solutions** for community to test
4. **Don't build full system** until issues resolved

**Either way, you've contributed valuable data to the project!**

---

## 📞 Questions?

- **Technical questions:** Open a GitHub Issue with label `validation-test`
- **Report results:** Open a GitHub Issue with label `build-report`
- **General discussion:** Use GitHub Discussions

Good luck with your testing! 🔬

---

*Document version: 1.0*  
*Last updated: October 30, 2025*
