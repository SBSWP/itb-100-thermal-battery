# Getting Started with ITB-100

**Welcome!** This guide helps you decide how to engage with this project based on your interests, skills, and resources.

---

## 🤔 Which Path Is Right for You?

### Path 1: 🔬 **Researcher / Student** (Validate the Science)

**Best if:**
- You have access to lab equipment (DSC, thermocouples, data logger)
- You're interested in phase-change materials or thermal storage
- You want data for a thesis, paper, or research project
- You have ~$200 budget and 4-6 weeks

**Start here:**
1. Read the [Validation Test Protocol](VALIDATION_TEST.md)
2. Order materials (~$180)
3. Build single-cell test rig
4. Run 50-cycle test over 4 weeks
5. Report results (positive or negative!)

**What you'll learn:**
- Does SAT chemistry work as claimed?
- Is electrochemical nucleation reliable?
- How does thermal performance compare to model?
- What are the failure modes?

**Time commitment:** ~40 hours over 4-6 weeks

---

### Path 2: 🛠️ **DIY Builder / Maker** (Build Full System)

**Best if:**
- You have metal fabrication skills (TIG welding, machining)
- You have shop access and tools
- You want thermal storage for your own home
- You have ~$3,500 budget and can dedicate weekends

**Start here:**
1. Read the full [technical documentation](models/ITB100_MODEL_DOCUMENTATION.md)
2. Review the [Bill of Materials](docs/BOM.md) *(to be created)*
3. Consider doing single-cell test first (recommended)
4. Build full system following [assembly guide](docs/assembly-guide.md) *(to be created)*
5. Install and monitor for 12+ months

**What you'll gain:**
- 16.7 kWh thermal storage system
- Real-world performance data
- Bragging rights as an early builder
- Contribution to building electrification

**Time commitment:** ~60 hours build + ongoing monitoring

---

### Path 3: 📊 **Engineer / Analyst** (Improve the Design)

**Best if:**
- You have expertise in thermal systems, heat transfer, or PCM
- You can do CAD modeling, FEA, or CFD analysis
- You want to optimize the design before anyone builds it
- You have access to simulation software

**Start here:**
1. Review the [system model code](models/itb100_system_model.py)
2. Study the [design documentation](models/ITB100_MODEL_DOCUMENTATION.md)
3. Identify improvement opportunities:
   - Heat exchanger geometry optimization
   - Alternative PCM formulations
   - Cost reduction strategies
   - Manufacturing process improvements

**Contributions needed:**
- Validated manufacturing cost estimates (quotes)
- FEA thermal analysis of heat exchanger
- Alternative PCM chemistry analysis
- Uncertainty quantification for performance predictions

**Time commitment:** 10-20 hours analysis + documentation

---

### Path 4: 💼 **Manufacturer / Entrepreneur** (Commercialize It)

**Best if:**
- You run a thermal equipment company
- You're an HVAC distributor or contractor
- You're looking for products in the building electrification space
- You have capital and want to bring this to market

**Start here:**
1. Review the [market analysis](analysis/EXECUTIVE_SUMMARY_PRODUCT_VIABILITY.md)
2. Study the competitive landscape (Sunamp, Steffes, etc.)
3. Get manufacturing quotes for 100/1,000/10,000 units
4. Build prototype for validation
5. Pursue UL certification if viable

**Questions to answer:**
- Can we hit $1,500 manufacturing cost at 1,000 units/year?
- What's the real market size (validate my TAM estimates)?
- Who are the right distribution partners?
- What's the certification timeline and cost?

**Next steps:**
- Contact me for collaboration discussion
- Build prototype with your manufacturing process
- Test market demand with HVAC installers

**Time commitment:** 6-12 month product development cycle

---

### Path 5: 🏡 **Homeowner** (Understand If This Solves Your Problem)

**Best if:**
- You have high heating costs (propane, oil, electric)
- You're considering a heat pump installation
- You're in a gas ban state (NY, CA, etc.)
- You want to understand if thermal storage makes sense

**Start here:**
1. Read the [use case analysis](analysis/HEAT_PUMP_ASSIST_SUMMARY.md)
2. Check if you match one of the target customer segments:
   - Cold climate heat pump owner
   - All-electric new construction
   - High TOU rate spread
   - Existing solar thermal system
3. Run the economic model for your location
4. Decide if you want to wait for commercial product or DIY

**Questions to ask:**
- What's my current heating cost per kWh?
- Do I have TOU electric rates? (Peak vs. off-peak spread?)
- Am I planning a heat pump installation?
- Do I have solar thermal collectors?

**If economics work for you:**
- Watch this project for builder results
- Contact local HVAC contractors about thermal storage
- Consider DIY build if you have skills

**Time commitment:** 2-3 hours research

---

### Path 6: 🌍 **Supporter** (Help Without Building)

**Best if:**
- You believe in building decarbonization
- You want to support open-source hardware
- You don't have time/skills to build but want to contribute
- You have connections or resources to share

**How to help:**
1. **⭐ Star the repository** (helps others discover it)
2. **Share the project** with relevant communities:
   - Building science forums
   - HVAC professional groups
   - Heat pump owner communities
   - University engineering departments
3. **Connect builders with resources:**
   - Know a contract manufacturer? Introduce them.
   - Know a thermal storage researcher? Share the project.
   - Have access to testing equipment? Offer it to builders.
4. **Provide feedback** on documentation (Is anything unclear?)
5. **Translate** documentation to other languages

**Time commitment:** 1-2 hours + ongoing as interested

---

## 🎯 Quick Decision Matrix

| Your Situation | Recommended Path | First Action |
|:---------------|:----------------|:-------------|
| **Student with lab access** | Path 1 (Researcher) | Read [VALIDATION_TEST.md](VALIDATION_TEST.md) |
| **Skilled DIYer with shop** | Path 2 (Builder) | Do validation test first |
| **Thermal engineer** | Path 3 (Analyst) | Review models, propose improvements |
| **HVAC manufacturer** | Path 4 (Commercialize) | Get manufacturing quotes |
| **Homeowner researching** | Path 5 (Understand) | Read use case analysis |
| **Want to help spread word** | Path 6 (Support) | Star repo, share with networks |

---

## 📚 Key Documents by Role

### Everyone Should Read:
- [README.md](README.md) - Main project overview
- [Executive Summary](analysis/EXECUTIVE_SUMMARY_PRODUCT_VIABILITY.md) - Market viability

### Researchers/Testers:
- [Validation Test Protocol](VALIDATION_TEST.md)
- [System Model](models/itb100_system_model.py)
- [Model Documentation](models/ITB100_MODEL_DOCUMENTATION.md)

### Builders:
- Bill of Materials *(to be added)*
- Assembly Guide *(to be added)*
- Safety Guidelines *(to be added)*

### Analysts:
- [System Model Code](models/itb100_system_model.py)
- [Market Analysis](models/itb100_market_analysis.py)
- [Heat Pump Use Case](models/heat_pump_assist_analysis.py)

### Manufacturers:
- [Market Analysis](analysis/EXECUTIVE_SUMMARY_PRODUCT_VIABILITY.md)
- Manufacturing cost model (in market analysis)
- Competitive landscape analysis

### Homeowners:
- [Heat Pump Assist Analysis](analysis/HEAT_PUMP_ASSIST_SUMMARY.md)
- Economic model results (by fuel type)

---

## 🚦 Project Status Check

Before diving in, understand where we are:

| Stage | Status | What This Means |
|:------|:------:|:----------------|
| **Design** | ✅ Complete | CAD models, thermal model, BOM all done |
| **Analysis** | ✅ Complete | Economics, market sizing, use cases analyzed |
| **Validation** | ⏳ Seeking builders | Need 3-5 people to test single-cell |
| **Prototype** | ⏳ Waiting | Full system build after validation |
| **Field Testing** | ⏳ Pending | 12-month monitoring after prototype |
| **Certification** | ❌ Not started | UL/CSA testing (if commercialized) |

**Translation:** The design is ready, but it's **unproven**. We need builders to validate core assumptions before anyone should invest $3,500 in a full system.

**Recommended:** Start with Path 1 (single-cell test) unless you're very risk-tolerant.

---

## ⚠️ Important Disclaimers

**Before proceeding, understand:**

❌ **This is NOT a certified product**
- No UL listing, no safety testing, no insurance approval
- Build and install at your own risk
- May void homeowner's insurance if not disclosed

❌ **Performance is NOT guaranteed**
- Based on models and literature, not field testing
- Real-world results may differ significantly
- No warranty or support

❌ **Permits likely required**
- Check local building codes before building
- May need plumbing permit, electrical permit
- Professional installation recommended for home integration

❌ **This is a research project**
- Goal is to validate (or invalidate) the concept
- Expect to encounter issues and debug
- You're an experimenter, not a customer

**By proceeding, you acknowledge these risks.**

---

## 📞 Getting Help

**Have questions about which path to choose?**

- **General questions:** [GitHub Discussions](../../discussions)
- **Specific issues:** [Open an Issue](../../issues)
- **Private inquiry:** Email maintainer (see [README](README.md))

**Want to connect with other builders?**

- Check [GitHub Discussions](../../discussions) for builder threads
- Look for existing test results in [Issues](../../issues)
- Consider starting a builder's Discord/Slack (community-organized)

---

## 🚀 Ready to Start?

Pick your path above and click the corresponding link to get started!

**Most common starting points:**

1. 🔬 **Researcher:** [Start with validation test →](VALIDATION_TEST.md)
2. 🛠️ **Builder:** Review BOM, build validation test first
3. 🏡 **Homeowner:** [Understand economics for your situation →](analysis/HEAT_PUMP_ASSIST_SUMMARY.md)
4. 🌍 **Supporter:** ⭐ Star the repo, share with others

---

**Remember:** Whether this works or fails, we learn together. Document your experience and share it with the community!

Good luck! 🎉

---

*Last updated: October 30, 2025*
