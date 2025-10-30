# ITB-100 Thermal Battery - Safety Guidelines

**⚠️ CRITICAL WARNING: This is an experimental thermal energy storage system that has NOT been tested, certified, or approved for residential use. Build and operate at your own risk.**

---

## 🚨 Overview of Hazards

The ITB-100 thermal battery involves multiple safety hazards:

1. **Thermal burns** - Working with fluids up to 90°C (194°F)
2. **Chemical hazards** - Handling sodium acetate and stabilizing chemicals
3. **Pressure hazards** - Sealed system with thermal expansion
4. **Electrical hazards** - Low voltage nucleation system and circulator pump
5. **Heavy equipment** - 280 kg system requires proper lifting/mounting
6. **Fire risk** - Electrical components near thermal insulation

**If you're uncomfortable with any of these hazards, DO NOT BUILD THIS SYSTEM.**

---

## 🔥 Thermal Hazards

### Operating Temperatures

| Component | Temperature | Risk Level |
|:----------|:-----------:|:----------:|
| SAT during charge | 65-90°C (149-194°F) | **HIGH** - Severe burns |
| SAT during discharge | 45-58°C (113-136°F) | **MODERATE** - Burns possible |
| Heat transfer fluid | 35-90°C (95-194°F) | **HIGH** - Severe burns |
| External surfaces | 30-50°C (86-122°F) | **LOW** - Uncomfortable to touch |

### Safety Measures

✅ **Required protective equipment:**
- Heat-resistant gloves (rated to 150°C minimum)
- Long sleeves and closed-toe shoes
- Safety glasses or face shield
- Apron or protective clothing

✅ **Installation requirements:**
- Install in area with fire-resistant flooring (concrete, tile - NOT carpet)
- Maintain 3 ft (1 m) clearance from combustible materials
- Do NOT install in occupied bedrooms or near sleeping areas
- Ensure adequate ventilation (especially during initial testing)

✅ **Emergency preparedness:**
- Keep first aid kit with burn treatment supplies nearby
- Know location of nearest cold water source for burn treatment
- Have fire extinguisher rated for electrical fires (Class C) within 10 ft
- Post emergency contact numbers visibly

⚠️ **Burn treatment:**
1. For thermal burns, immediately cool with room-temperature water for 10-20 minutes
2. Do NOT use ice (can cause further tissue damage)
3. Seek medical attention for burns larger than 2 inches or on face/hands/joints
4. For severe burns, call 911 immediately

---

## ⚗️ Chemical Hazards

### Materials Used

| Chemical | Quantity | Hazard Classification | Primary Risks |
|:---------|:--------:|:---------------------:|:--------------|
| **Sodium Acetate Trihydrate (SAT)** | 227 kg | Irritant | Eye/skin irritation, ingestion hazard |
| **Sodium Polymethacrylate (Na-PMAA)** | 1.5 kg | Irritant | Skin/eye irritation, respiratory irritant |
| **Disodium Phosphate (Na₂HPO₄)** | 4.5 kg | Irritant | Eye irritation, gastrointestinal issues if ingested |
| **Propylene Glycol (optional)** | 4 L | Low toxicity | Skin irritant, slippery if spilled |
| **Thermal Epoxy** | 400 g | Sensitizer | Skin sensitization, strong odor |

### Safety Data Sheets (SDS)

📄 **CRITICAL:** Download and read SDS for ALL chemicals before use:
- Sodium Acetate Trihydrate: [Lab Alley](https://www.laballey.com), [Bulk Reef Supply](https://www.bulkreefsupply.com)
- Na-PMAA: Request from supplier
- Disodium Phosphate: [ChemWorld](https://chemworld.com)
- Arctic Alumina Epoxy: [Arctic Silver website](https://www.arcticsilver.com)

### Chemical Handling Procedures

✅ **Personal Protective Equipment (PPE):**
- Chemical-resistant gloves (nitrile or neoprene)
- Safety glasses with side shields
- Dust mask (N95) when handling dry powders
- Lab coat or chemical-resistant apron
- Work in well-ventilated area

✅ **Mixing procedures:**
- Always add chemicals to water, NEVER water to chemicals
- Mix in properly sized containers with adequate freeboard (30% minimum)
- Use magnetic stirrer or low-speed paddle (avoid splashing)
- Keep mixing area clear of ignition sources (SAT is not flammable, but epoxy vapors are)
- Have spill cleanup materials ready (absorbent, broom, trash bags)

✅ **Storage requirements:**
- Store SAT in sealed containers away from moisture
- Keep stabilizers in original containers with labels intact
- Store in cool, dry location away from incompatible materials
- Keep out of reach of children and pets
- Label all containers clearly with contents and date

⚠️ **Exposure response:**
- **Skin contact:** Wash with soap and water for 15 minutes
- **Eye contact:** Flush with water for 15 minutes, seek medical attention
- **Ingestion:** Do NOT induce vomiting. Drink water and call Poison Control: 1-800-222-1222
- **Inhalation:** Move to fresh air, seek medical attention if symptoms persist

### Spill Response

**Small spills (<1 kg):**
1. Ventilate area
2. Wear appropriate PPE
3. Absorb with paper towels or absorbent material
4. Dispose in sealed plastic bag in regular trash (SAT is not hazardous waste)
5. Clean area with damp mop

**Large spills (>10 kg):**
1. Evacuate area and ventilate
2. Prevent spill from entering drains
3. Contact local hazmat team if >100 kg spilled
4. Absorb with commercial absorbent or kitty litter
5. Shovel into waste containers
6. Dispose according to local regulations

---

## 💥 Pressure Hazards

### System Pressures

| Component | Normal Pressure | Maximum Pressure | Relief Setting |
|:----------|:---------------:|:----------------:|:--------------:|
| Heat exchanger loop | 5-10 PSI | 50 PSI (design) | 30 PSI |
| SAT pouches | Atmospheric | N/A (vented during filling) | N/A |
| Expansion tank | 12 PSI (pre-charge) | 30 PSI | 30 PSI |

### Pressure Safety

✅ **Required components:**
- Pressure relief valve (30 PSI) installed on highest point of loop
- Expansion tank properly sized (2 gallon minimum)
- Pressure gauge visible during operation
- Air bleeder valve at high points

✅ **Pre-operation checks:**
- Visually inspect all fittings for leaks
- Perform pressure test at 1.5× operating pressure (15 PSI) for 1 hour
- Verify pressure relief valve operation (manual test)
- Check expansion tank pre-charge pressure (should be 12 PSI)

⚠️ **Overpressure response:**
- If pressure exceeds 20 PSI, immediately shut off heat source
- Allow system to cool naturally (do NOT add cold water)
- Investigate cause (failed relief valve, undersized expansion tank, blockage)
- Do NOT restart until issue resolved

⚠️ **Leak response:**
- Small leak: Shut down system, allow to cool, repair leak before restarting
- Large leak: Shut off power, ventilate area, contain spill, check for burn hazards
- Steam leak: Evacuate area immediately, shut off power from safe distance, call for help

---

## ⚡ Electrical Hazards

### Electrical Systems

| Component | Voltage | Current | Hazard Level |
|:----------|:-------:|:-------:|:------------:|
| Nucleation system | 1.5V DC | 5A | **LOW** - Minor shock risk |
| Circulator pump | 120V AC | 1.5A | **MODERATE** - Shock/electrocution risk |
| Arduino controller | 5V DC | 0.5A | **VERY LOW** - Minimal risk |

### Electrical Safety

✅ **Installation requirements:**
- All 120V AC wiring must be performed by licensed electrician OR following NEC code
- Use GFCI-protected outlet for circulator pump (required)
- Keep all electrical components outside of enclosure (above freezer)
- Use waterproof enclosures for all electrical components in damp areas
- Properly ground all metal components

✅ **Low-voltage DC system (nucleation):**
- Maximum 1.5V DC output (safe voltage, no shock hazard)
- Fuse protection: 5A slow-blow fuse in line with power supply
- Keep wiring organized and secured with zip ties
- Use insulated connectors rated for 150°C

✅ **Circulator pump:**
- Must be connected to GFCI outlet (test monthly)
- Keep pump dry (mount above water level if possible)
- Check cord for damage monthly
- Replace immediately if any damage to cord or housing

⚠️ **Electrical failure response:**
- If GFCI trips repeatedly, do NOT reset - investigate cause
- If pump makes unusual noise or smells, shut off immediately
- If any sparking or smoking, shut off breaker and call electrician
- Never touch electrical components with wet hands

---

## 🏋️ Physical Hazards

### Weight and Handling

**Fully assembled system weight: 280 kg (617 lbs)**
- PCM (SAT): 227 kg
- Heat exchanger assembly: 28 kg
- Enclosure (freezer): 25 kg

✅ **Safe lifting procedures:**
- **NEVER lift alone** - Requires 3-4 people or mechanical assistance
- Use proper lifting technique (lift with legs, not back)
- Consider using appliance dolly or pallet jack
- Ensure floor can support weight (concrete slab ideal)
- Check floor joists if installing on upper floor (may require structural evaluation)

✅ **Installation location:**
- Place on level, stable surface
- Ensure floor can support 100 lbs/sq ft minimum
- Keep away from stairs or edges
- Bolt to floor if in earthquake-prone area
- Consider secondary containment (drip pan) for leak protection

⚠️ **Tipping hazard:**
- Top-heavy design when lid is open
- Never stand or sit on unit
- Keep children away from unit
- Consider adding anti-tip bracket if in household with children

---

## 🔥 Fire Safety

### Fire Risks

**Low fire risk overall**, but consider:
- Electrical short in pump or control system
- Insulation in contact with overheated surfaces
- Thermal runaway if overcharged

✅ **Fire prevention:**
- Use only UL-listed electrical components
- Keep combustible materials 3 ft away
- Install smoke detector within 10 ft of unit
- Never bypass safety controls (thermostat, pressure relief)
- Inspect wiring quarterly for damage

✅ **Fire suppression:**
- Keep ABC or BC fire extinguisher within 10 ft
- Never use water on electrical fire
- If fire occurs, shut off power at breaker and call 911
- Evacuate if fire spreads beyond containment

---

## 🛠️ Construction Safety

### Fabrication Hazards

**During build phase:**

✅ **Metalworking safety:**
- Wear safety glasses when cutting/drilling aluminum
- Use hearing protection with power tools
- Secure workpieces properly before drilling
- Deburr all sharp edges
- Wear cut-resistant gloves when handling aluminum plates

✅ **Chemical mixing safety:**
- Work in well-ventilated area or outdoors
- Never heat chemicals in sealed container
- Use heat-resistant container for mixing SAT
- Keep fire extinguisher nearby when using heat sources
- Avoid breathing vapors from thermal epoxy

✅ **Heat sealing safety:**
- Use impulse sealer on insulated surface
- Keep hands clear of sealing element (reaches 200°C)
- Allow sealer to cool before touching
- Unplug when not in use

---

## 🏥 First Aid

### Essential First Aid Supplies

Keep these items accessible:
- Burn gel or aloe vera
- Sterile gauze pads (various sizes)
- Medical tape
- Cold packs
- Eye wash solution
- Nitrile gloves
- CPR mask
- First aid manual

### Emergency Contacts

**Post these numbers visibly near the system:**
- Emergency services: **911**
- Poison Control Center: **1-800-222-1222**
- Fire Department (non-emergency): _(fill in your local number)_
- Licensed electrician: _(fill in contact info)_
- HVAC technician: _(fill in contact info)_

---

## 🔍 Pre-Operation Checklist

Before first operation, verify:

- [ ] All pressure fittings tightened and leak-tested
- [ ] Pressure relief valve installed and functional
- [ ] GFCI outlet tested and operational
- [ ] Fire extinguisher present and charged
- [ ] First aid kit stocked
- [ ] Smoke detector installed and tested
- [ ] Area around unit clear of combustibles
- [ ] All SDS sheets downloaded and available
- [ ] Emergency contact numbers posted
- [ ] Another person present during first heat cycle

---

## 📋 Maintenance Safety

### Monthly Inspections

- [ ] Check for leaks (visual inspection of all fittings)
- [ ] Test GFCI outlet
- [ ] Inspect pump power cord for damage
- [ ] Check pressure gauge reading (should be 5-10 PSI)
- [ ] Verify smoke detector operation

### Quarterly Inspections

- [ ] Test pressure relief valve (manual lift test)
- [ ] Inspect expansion tank for corrosion
- [ ] Check aluminum plates for corrosion (if accessible)
- [ ] Inspect electrical connections for looseness/corrosion
- [ ] Review and update emergency contact list

### Annual Inspections

- [ ] Drain and flush heat transfer loop
- [ ] Replace expansion tank if corroded
- [ ] Test nucleation system (all electrodes)
- [ ] Inspect insulation for degradation
- [ ] Professional electrical inspection (recommended)

---

## 🚫 What NOT To Do

**NEVER:**
- ❌ Leave system unattended during first 5 heating cycles
- ❌ Bypass safety controls or pressure relief valve
- ❌ Open system while pressurized or hot
- ❌ Use flammable fluids in heat transfer loop
- ❌ Allow children unsupervised access to system
- ❌ Install without proper clearances
- ❌ Modify pressure relief valve or expansion tank
- ❌ Use damaged electrical components
- ❌ Mix chemicals without proper PPE
- ❌ Dispose of SAT down drains (check local regulations)

---

## ⚖️ Legal Disclaimers

**Building Permits:**
- Check with local building department before installation
- May require plumbing permit, electrical permit, or mechanical permit
- Some jurisdictions prohibit uncertified thermal storage systems

**Insurance:**
- Notify homeowner's insurance about installation
- Uncertified systems may void coverage - verify before building
- Consider additional liability coverage

**Liability:**
- This design is provided AS-IS with no warranty
- You assume all risk by building and operating this system
- Designer/contributors accept no liability for injury, property damage, or death
- Not certified for commercial installation
- Use at your own risk

**Code Compliance:**
- This system does NOT comply with UL 2596 (Energy Storage Systems)
- Not approved for residential use by any certification body
- May violate local fire codes - check before installing

---

## 📚 Additional Resources

**Safety Standards:**
- NFPA 1 (Fire Code)
- NEC Article 690 (Solar Systems)
- ASME Boiler & Pressure Vessel Code (Section VIII)
- OSHA Chemical Hazard Communication Standard

**Training:**
- Consider taking Red Cross First Aid/CPR course
- HVAC safety training (available online)
- Electrical safety training

**Monitoring:**
- Consider adding temperature monitoring with alarms
- Install leak detection sensors below unit
- Use smart plug with remote shutoff capability

---

## ❓ Questions or Concerns?

**If you are uncomfortable with any aspect of this project, STOP and consult with:**
- Licensed electrician
- Licensed plumber
- HVAC professional
- Fire safety inspector
- Structural engineer (for floor loading)

**It is always better to be safe than sorry.**

---

*Last updated: October 30, 2025*
*Safety information is subject to change - always consult current safety standards and local codes.*

**⚠️ REMEMBER: This is an experimental system. Build and operate at your own risk.**
