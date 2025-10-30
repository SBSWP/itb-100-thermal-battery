# Contributing to ITB-100 Thermal Battery

Thank you for your interest in contributing to this project! This is an open research effort to validate and improve affordable thermal energy storage for building electrification.

## 🎯 Project Goals

1. **Validate the design** through real-world testing
2. **Improve performance** with better materials, geometry, or chemistry
3. **Reduce costs** through manufacturing optimization
4. **Document learnings** so the community benefits whether it succeeds or fails
5. **Maintain openness** — all improvements remain open-source

## 🤝 How to Contribute

### Types of Contributions We Need

#### 1. **Test Builders** (Highest Priority)

If you build a prototype (single-cell or full system):

**What to share:**
- Build photos and documentation
- Performance measurements (power output, temperatures, cycle counts)
- Any deviations from the design (and why)
- Problems encountered and how you solved them
- Cost breakdown (actual vs. estimated)

**How to share:**
- Open a GitHub Issue with the label `build-report`
- Include photos in `/builds/[your-username]/` directory
- Submit data as CSV or JSON files
- Write a summary in Markdown

**Example structure:**
```
/builds/john-doe-2026/
├── README.md              # Build summary
├── photos/                # Progress photos
├── data/                  # Performance measurements
│   ├── cycle-test-data.csv
│   └── temperature-profiles.csv
└── lessons-learned.md     # What worked, what didn't
```

#### 2. **Researchers & Engineers**

If you have expertise in:
- Phase-change materials
- Heat exchanger design
- Thermal system modeling
- Manufacturing processes
- Building HVAC systems

**What to contribute:**
- Technical analysis of the design
- Alternative PCM formulations
- Heat exchanger geometry improvements
- Manufacturing cost estimates
- Integration strategies

**How to contribute:**
- Open an Issue with the label `research`
- Submit Pull Requests for model improvements
- Share papers or references we should know about

#### 3. **Documentation Improvements**

Help make this easier for others to understand and build:

- Clarify confusing sections
- Add safety warnings where needed
- Improve assembly instructions
- Translate to other languages
- Create video tutorials or diagrams

**How to contribute:**
- Submit Pull Requests to `/docs/`
- Open Issues for unclear sections
- Share external content (videos, blog posts)

#### 4. **Software & Analysis**

Improve the modeling and analysis tools:

- Enhance the thermal model accuracy
- Add uncertainty quantification
- Create design optimization tools
- Build web-based calculators
- Improve data visualization

**How to contribute:**
- Submit Pull Requests to `/models/`
- Follow PEP 8 style for Python code
- Include docstrings and unit tests
- Update documentation

## 📋 Contribution Guidelines

### Before You Start

1. **Search existing Issues** to avoid duplication
2. **Read the documentation** thoroughly
3. **Start small** — comment on Issues before diving into major work
4. **Ask questions** — use GitHub Discussions for general questions

### Pull Request Process

1. **Fork the repository** and create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** with clear, descriptive commits
   ```bash
   git commit -m "Add improved SAT nucleation analysis"
   ```

3. **Test your changes** if applicable (models should run without errors)

4. **Update documentation** to reflect your changes

5. **Submit a Pull Request** with:
   - Clear description of what you changed and why
   - Reference any related Issues
   - Photos/data if relevant
   - Note any breaking changes

6. **Respond to feedback** — maintainers may suggest changes

### Code Standards

**Python:**
- Follow PEP 8 style guide
- Use type hints where appropriate
- Include docstrings for functions/classes
- Add comments for complex logic
- Keep functions focused and modular

**Documentation:**
- Use Markdown formatting
- Include tables and diagrams where helpful
- Write clearly for DIY builders (not just engineers)
- Add units to all physical quantities
- Include safety warnings where relevant

**CAD/Design Files:**
- Provide STEP format (universal)
- Include source files (Fusion 360, SolidWorks, etc.) if possible
- Add assembly instructions for complex parts
- Include material specifications

## 🔬 Validation Testing Protocol

If you're building a test unit, here's what we need to validate:

### Critical Metrics

1. **SAT Chemistry Stability**
   - Cycle count before degradation
   - Visual appearance after 50+ cycles
   - DSC measurement of latent heat capacity
   - Phase separation behavior

2. **Nucleation Reliability**
   - Success rate (%) over 50 attempts
   - Electrode voltage and current
   - Time to crystallization after trigger
   - Any auto-nucleation events

3. **Thermal Performance**
   - Measured UA value (W/K)
   - Power output vs. time profile
   - Charge and discharge efficiency
   - Temperature uniformity

4. **Mechanical Durability**
   - Pouch integrity after cycling
   - Aluminum plate corrosion
   - Thermal epoxy bond strength
   - Pressure vessel integrity

### Data Collection

**Minimum data to collect:**
- Temperature sensors: SAT bulk, plate surface, water inlet/outlet
- Flow rate: Constant or measured
- Time stamps: Charge start/end, discharge start/end
- Ambient conditions: Room temperature
- Cycle count: Total number of charge/discharge cycles

**Preferred data collection:**
- High-frequency logging (1 sample/minute)
- CSV format with timestamps
- Include sensor calibration info
- Note any anomalies or manual interventions

**Share your data:**
```
/data/builds/[your-username]/
├── README.md                    # Test conditions
├── cycle-001.csv               # First cycle data
├── cycle-050.csv               # 50th cycle data
└── dsc-measurements.pdf        # Lab analysis results
```

## 🚫 What We Don't Accept

To keep this project focused and useful:

❌ **Closed-source improvements** — All contributions must remain MIT licensed  
❌ **Proprietary materials** — Don't require expensive or patented components  
❌ **Unsafe practices** — No shortcuts that compromise safety  
❌ **Unsubstantiated claims** — Back up performance claims with data  
❌ **Commercial promotion** — This is a research project, not a marketplace  

## 🏆 Recognition

Contributors will be recognized in:
- The main README.md (Contributors section)
- Release notes for significant contributions
- Academic papers if this leads to publications

We believe in giving credit where credit is due!

## 📞 Getting Help

**Have questions?**
- **General discussion:** Use GitHub Discussions
- **Specific issues:** Open a GitHub Issue
- **Private matters:** Email the maintainer (see README)

**Want to collaborate more deeply?**
- Some contributors may want to co-author papers
- Manufacturing partnerships are possible
- We're open to grant applications for research

## 🎓 Learning Resources

If you're new to thermal storage or phase-change materials:

**Introductory:**
- [MIT OpenCourseWare: Thermal Energy Storage](https://ocw.mit.edu)
- [DOE Building Technologies Office: Thermal Storage Overview](https://www.energy.gov)

**Advanced:**
- Mehling & Cabeza: "Heat and Cold Storage with PCM" (textbook)
- Lane: "Solar Heat Storage: Latent Heat Materials" (classic reference)
- Recent papers on SAT stabilization (see README references)

**HVAC Integration:**
- ASHRAE Handbook: HVAC Systems and Equipment
- Building Science Corporation: [buildingscience.com](https://buildingscience.com)

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

**In summary:**
- Be respectful and inclusive
- Welcome newcomers and different perspectives
- Focus on what's best for the project
- Accept constructive criticism gracefully
- Show empathy toward other community members

Violations can be reported to the project maintainer.

## 🌟 Why Contribute?

**For researchers:**
- Collaborate on a real-world thermal storage project
- Access to field test data
- Potential for publications

**For builders:**
- Solve your own heating problem
- Learn about phase-change materials
- Join a community of experimenters

**For manufacturers:**
- Evaluate commercial viability
- Validate costs and performance
- Build relationships with early adopters

**For everyone:**
- Contribute to building decarbonization
- Advance open-source hardware
- Learn something new

## 🚀 Next Steps

Ready to contribute?

1. **Star the repository** ⭐ (helps others find it)
2. **Introduce yourself** in GitHub Discussions
3. **Pick an Issue** labeled `good first issue` or `help wanted`
4. **Ask questions** — we're here to help!

Thank you for considering contributing to ITB-100!

---

*Last updated: October 30, 2025*
