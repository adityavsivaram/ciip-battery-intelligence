# CIIP Battery Intelligence Framework
### Cross-Industry Input Pressure — India's Critical Mineral Supply Chain Risk Model

[![Framework Version](https://img.shields.io/badge/Framework-v4.1-gold)](./reports/)
[![Methodology](https://img.shields.io/badge/Methodology-Leontief_I--O-blue)](./methodology/METHODOLOGY.md)
[![Data Confidence](https://img.shields.io/badge/Data_Tiers-A_%7C_B_%7C_C-green)](./methodology/DATA_CONFIDENCE.md)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](./LICENSE)

---

## What This Framework Is

The **CIIP Battery Intelligence Framework** is an industrial dependency intelligence model for India's electrification-era supply chains. It answers one question:

> *"What second-order industrial dependencies emerge when a civilisation electrifies?"*

This is **not** a commodity price forecast. It is a **strategic dependency analysis** that maps structural chokepoints at the molecular processing level, applies **Ultimate Beneficiary Ownership (UBO) Risk** methodology to correct country-of-origin misclassification, and tracks industrial contagion propagation through three-wave Leontief mechanics.

---

## The Central Finding

India is not reducing import risk through its clean energy transition. It is performing a **risk substitution** — trading a visible, liquid, manageable commodity dependency (oil) for an invisible, concentrated, and structurally locked-in processing dependency (battery minerals and solar inputs).

The supplier changes from Riyadh to Beijing. The leverage does not reduce. It becomes structurally difficult and economically costly to exit within short industrial timelines.

This is not a daily operational fuel trap. It is an **industrial expansion chokepoint** — the failure mode is CapEx stranding, not petrol queues.

---

## Framework Architecture

### Theoretical Basis
- **Leontief Input-Output Economics** (Nobel Prize, 1973)
- Three-wave industrial contagion propagation model
- Expert-calibrated scoring with PCA-informed weight rationale
- Ultimate Beneficiary Ownership (UBO) Risk methodology

### CIIP Scoring Formula
```
CIIP Score = (EV Demand × 0.35) + (Cross-Industry Competition × 0.40) + (Geopolitical Risk × 0.25) × (10/3)
```

Weights are **expert-calibrated** on a Leontief I-O theoretical basis. PCA statistical validation is on the 90-day empirical upgrade roadmap (see [METHODOLOGY.md](./methodology/METHODOLOGY.md)).

### Six Critical Materials Scored

| Material | CIIP Score | Risk Tier | Primary Sectors |
|----------|-----------|-----------|-----------------|
| Nickel | **10.0** | 🔴 CRITICAL | EV batteries + stainless steel + aerospace turbine blades |
| Lithium | **8.8** | 🔴 CRITICAL | EV batteries + grid storage + consumer electronics |
| Polysilicon | **8.7** | 🔴 CRITICAL | Solar PV + semiconductors + optoelectronics |
| Cobalt | **7.8** | 🟠 HIGH | EV batteries (NMC) + aerospace alloys + defence |
| Graphite | **7.4** | 🟠 HIGH | Battery anode + steelmaking + nuclear moderator |
| Manganese | **6.1** | 🟡 MEDIUM | NMC batteries + steel alloys + fertiliser |

---

## Key Analytical Contributions (v4.1)

### 1. pCAM Molecular Chokepoint
The framework documents the **NaOH/NH₄OH co-precipitation mechanism** that makes India's "domestic" cathode precursor plants an optical illusion. An Indian pCAM reactor converts imported Chinese-processed metal sulphates (NiSO₄, CoSO₄, MnSO₄) into mixed hydroxide powder. The domestic value addition is the precipitation step. The strategic value addition is effectively zero — the leverage resides in the metal sulphate inputs, which China controls at 75-82% of global sulphation capacity.

### 2. Ultimate Beneficiary Ownership (UBO) Risk
Country-of-origin certificates are customs instruments, not risk instruments. This framework introduces **UBO Risk** as a named methodology:

> *"The supply chain vulnerability created when the corporate entity that makes production, pricing, and allocation decisions for a critical industrial input is beneficially owned or operationally controlled by a foreign state-linked conglomerate — regardless of the geographic location of the physical asset or the national flag on the shipping certificate."*

**Live UBO examples:**
- Indonesian HPAL plants → Indonesian export certificate → **Chinese UBO** (Tsingshan, Huayou Cobalt)
- Belgian NiSO₄ (Umicore) → Belgian corporate entity → **Mixed UBO** (feedstock: Russian/African-Chinese)
- DRC cobalt (Tenke, Kisanfu) → DRC origin → **Chinese UBO** (CMOC)
- Australia BHP Nickel West → Australian origin → **Western UBO** (genuine benchmark)

### 3. Nickel Variant A / Variant B Split
Based on IEEFA/ICRIER trade data (Tier A):
- **Variant A** (Nickel Oxides/Hydroxides/MHP): India sources **64.7% from Australia** — but Indonesian component is Chinese-HPAL-owned
- **Variant B** (Nickel Sulphate NiSO₄): India sources **65%+ from Belgium** — genuine first-order diversification, but feedstock carries Russian/African-Chinese UBO exposure

### 4. J&K Lithium — Policy Delusion, Not Paradox
India's 5.9 million tonne J&K lithium occurrence is classified **G3/G4 under UNFC** — reconnaissance-level geological evidence, unbankable under JORC/NI 43-101/SAMREC. The deposit is a **sedimentary claystone** — a formation type with no proven commercial extraction technology globally as of 2026 (Thacker Pass, Nevada — the closest comparable — began permitting in 2016 and reached first production a decade later). Realistic minimum timeline to battery-grade output: **13–20 years**. Citing J&K as a near-term strategic offset to Chinese processing dominance is not optimism. It is a classification error dressed as policy.

### 5. Chemistry Longevity Clause
The framework is an **Inflexible Infrastructure Dependency Matrix**, not a lithium or nickel calculator. Whether the cathode is NMC, LFP, or layered oxide sodium-ion, the manufacturing pathway requires: sulphated metal precursors → NaOH/NH₄OH co-precipitation → controlled atmosphere calcination → dry room cell assembly → formation cycling. China controls the majority of global capacity at every one of these steps. Chemistry transition **relocates** the dependency; it does not exit it.

### 6. Growth Chokepoint vs Daily Fuel Trap
Oil dependency = **flow disruption risk** (recoverable in weeks).
Critical mineral dependency = **industrial expansion chokepoint** (recoverable in years to decades).
The failure mode is CapEx stranding — a committed gigafactory that cannot operate because its precursor chemical supply is redirected by Chinese corporate ownership decisions, not government export controls.

---

## Repository Structure

```
ciip-battery-intelligence/
│
├── README.md                          ← This file
├── LICENSE
│
├── reports/                           ← Published deliverables
│   ├── CIIP_Battery_Intelligence_v4_1_Final.pdf     ← Full intelligence report
│   ├── CIIP_Battery_Case_Study_v4_1_Final.html      ← Interactive case study
│   ├── CIIP_Battery_Executive_Deck.pptx             ← Executive presentation
│   └── version_history/
│       ├── v1_CIIP_Battery_Case_Study.html
│       ├── v2_CIIP_Battery_Case_Study.html
│       ├── v3_CIIP_Battery_Case_Study.html
│       └── v4_CIIP_Battery_Case_Study.html
│
├── src/                               ← Python scoring engine
│   ├── ciip_scoring_engine.py         ← Core CIIP scoring model
│   ├── ubo_risk_classifier.py         ← UBO Risk classification module
│   ├── leontief_propagation.py        ← I-O contagion propagation model
│   └── scenario_simulator.py          ← Four-scenario stress test engine
│
├── data/                              ← Data infrastructure
│   ├── README_data.md                 ← Data collection guide
│   ├── raw/                           ← Source data (Stage 2 collection in progress)
│   │   ├── usgs_nickel_production_2015_2025.csv
│   │   ├── usgs_lithium_production_2015_2025.csv
│   │   └── [additional USGS files]
│   └── processed/
│       ├── hhi_concentration_index.csv
│       └── ciip_scores_master.csv
│
├── methodology/                       ← Analytical documentation
│   ├── METHODOLOGY.md                 ← Full scoring methodology
│   ├── DATA_CONFIDENCE.md             ← Tier A/B/C classification framework
│   ├── UBO_RISK_FRAMEWORK.md          ← UBO methodology documentation
│   └── PCA_UPGRADE_ROADMAP.md         ← Statistical validation pathway
│
└── assets/                            ← Supporting materials
    └── ciip_framework_lineage.md      ← CIIP v1.0 → v4.1 evolution
```

---

## Framework Lineage

| Version | Sector | Materials | Central Contribution |
|---------|--------|-----------|---------------------|
| CIIP v1.0 | Pharma / Indian API | Soda ash, methanol, acetic acid | Cross-industry contagion — agrochemical kharif season competing with pharma API solvents |
| CIIP-L / POIS | Predictive Operations | All upstream inputs | Leading indicator framework — 6–8 weeks upstream monitoring |
| Ghost Tier | Pharma sub-tier | API precursors | Approved supplier list concentration risk |
| **CIIP Battery v4.1** | **EV + Solar + Aerospace** | **Ni, Li, Co, polysilicon, graphite, Mn** | **India's green transition builds a deeper import trap — molecular-level proof** |

---

## Data Confidence Classification

Every claim in this framework carries a tier:

| Tier | Definition | Examples |
|------|-----------|---------|
| 🟢 **Tier A** | Institutionally verified, primary source, cross-referenced | India oil import $116.4B (IEEFA 2026) · Indonesia nickel 67%+ (USGS 2025) · China LFP cathode 98% (IEA 2025) |
| 🟠 **Tier B** | Derived analytical estimate with stated assumptions | CIIP scores · Leontief multipliers · Layer 2a–2e capacity estimates |
| 🔴 **Tier C** | Strategic scenario assumption — directional, bounded | 2030 import bill projections · Chemistry pathway sensitivity ranges |

---

## Empirical Upgrade Roadmap

### Current State (v4.1) — Expert-Calibrated
Scores are expert-calibrated on Leontief I-O theoretical basis. PCA has **not yet been executed** on this dataset.

### 30-Day Target
- [ ] USGS 2015–2025 production data — HHI concentration index for all 6 materials
- [ ] UN Comtrade API — India import data by material and source country
- [ ] LME nickel/cobalt 10-year monthly price series
- [ ] UBO-adjusted concentration index (ownership vs origin)

### 90-Day Target (v4.2)
- [ ] PCA on assembled panel — empirically derived dimension weights
- [ ] Backtest CIIP scores against 15 documented supply disruption events (2015–2025)
- [ ] HHI-derived geopolitical score replacing qualitative assessment
- [ ] Scenario stress test engine with four chemistry pathway assumptions

### 12-Month Target (v5.0)
- [ ] Directed graph using NetworkX — betweenness centrality analysis
- [ ] Monte Carlo simulation — confidence intervals for all scores
- [ ] Dependency elasticity analysis — India industrial output per $1B supply disruption
- [ ] Framework extension: AI infrastructure, semiconductors, fertiliser minerals
- [ ] India 2030 Operational Resilience Map

---

## How to Use the Scoring Engine

```python
from src.ciip_scoring_engine import CIIPScorer

scorer = CIIPScorer()

# Score a material
result = scorer.score(
    material="nickel",
    ev_demand=3.0,
    cross_industry=3.0,
    geopolitical=3.0
)
print(result)
# {'material': 'nickel', 'score': 10.0, 'tier': 'CRITICAL',
#  'ev_weight': 0.35, 'cross_weight': 0.40, 'geo_weight': 0.25}

# Run scenario stress test
from src.scenario_simulator import ScenarioSimulator
sim = ScenarioSimulator()
scenarios = sim.run_all_scenarios()
```

---

## Run the Interactive Case Study Locally

```bash
# Clone the repository
git clone https://github.com/adityavsivaram/ciip-battery-intelligence.git
cd ciip-battery-intelligence

# Open the interactive HTML case study
open reports/CIIP_Battery_Case_Study_v4_1_Final.html

# Or run the Python scoring engine
pip install -r requirements.txt
python src/ciip_scoring_engine.py
```

---

## Publications & Related Work

- **India Supply Chain Signals** — Substack: [indiasupplychainsignals.substack.com](https://indiasupplychainsignals.substack.com)
- **CIIP Pharma Framework** — [github.com/adityavsivaram/ciip-pharma-supply-chain-intelligence](https://github.com/adityavsivaram/ciip-pharma-supply-chain-intelligence)
- **Issue 1** — Cross-industry contagion in Indian pharma API supply chains
- **Issue 2** — From reactive to predictive: leading indicator frameworks

---

## Author

**Aditya V Sivaram Poduri**
Deputy Manager — Information Systems, NCC Limited (India's largest EPC/infrastructure company)
MS Data Science — Scaler School of Technology
Oxford Advanced Business Analytics with AI (completion September 2026)
TÜV SÜD Six Sigma Green Belt | Google Data Analytics Professional Certificate

*21+ years operational experience across 50+ Indian infrastructure project sites — the ground-truth foundation that makes this framework operationally credible rather than theoretically abstract.*

**Connect:**
- LinkedIn: [linkedin.com/in/adityavsivaram](https://linkedin.com/in/adityavsivaram)
- Substack: [indiasupplychainsignals.substack.com](https://indiasupplychainsignals.substack.com)
- GitHub: [github.com/adityavsivaram](https://github.com/adityavsivaram)

---

## Citation

If you use this framework in research or analysis:

```
Poduri, A.V.S. (2026). CIIP Battery Intelligence Framework v4.1:
India's Green Import Trap — Cross-Industry Input Pressure Analysis
for Electrification-Era Supply Chains. India Supply Chain Signals.
https://github.com/adityavsivaram/ciip-battery-intelligence
```

---

## License

MIT License. See [LICENSE](./LICENSE) for details.
Framework concept, UBO Risk methodology, and analytical contributions are original intellectual property of Aditya V Sivaram Poduri.
