# CIIP Battery Intelligence Framework — Methodology Documentation

## Version History
- v4.1 — June 2026 — Current (expert-calibrated, PCA-informed roadmap)
- v4.0 — June 2026 — Six research exchange upgrades integrated
- v3.0 — June 2026 — Institutional upgrade (data confidence tiers, Leontief operationalised)
- v2.0 — June 2026 — Scenario architecture, chemistry conditionality added
- v1.0 — June 2026 — Initial battery materials framework

---

## 1. Theoretical Foundation

### Leontief Input-Output Economics
The CIIP framework is grounded in Wassily Leontief's Input-Output economics (Nobel Prize, 1973). The I-O framework models how industries depend on each other's outputs as inputs, making supply disruptions propagate through the industrial system rather than staying contained to a single sector.

In the battery materials context:
- **Rows** = critical input materials (nickel, lithium, polysilicon, cobalt, graphite, manganese)
- **Columns** = industrial sectors consuming those inputs (EV batteries, solar PV, stainless steel, aerospace, grid storage, electronics)
- **Cell values** = import dependency coefficients (0 to 1.0 scale)

### Three-Wave Contagion Propagation
Following Leontief I-O mechanics, supply disruptions propagate in three waves:

| Wave | Timeframe | Mechanism |
|------|-----------|-----------|
| Wave 1 — Direct | Days 0–30 | Sectors immediately deprived of the input |
| Wave 2 — Indirect | Days 30–90 | Sectors depending on Wave 1 sectors (multiplied by Leontief coefficient) |
| Wave 3 — Induced | Months 3–12 | Economy-wide CapEx and investment confidence effects |

### Leontief Output Multipliers (Tier B — Expert Estimated)
| Material | Output Multiplier | Basis |
|----------|------------------|-------|
| Nickel | 2.8× | RBI I-O tables + OECD TiVA proxy |
| Polysilicon | 2.6× | Solar sector I-O linkages |
| Lithium | 2.4× | Battery sector upstream-downstream |
| Cobalt | 1.9× | Aerospace + EV combined |
| Graphite | 1.7× | Anode + steel sector |
| Manganese | 1.4× | Steel sector primary linkage |

*India-specific I-O table has not yet been constructed. Current values use OECD TiVA as proxy. Building an India-specific table is a 12-month target.*

---

## 2. CIIP Scoring Formula

```
CIIP Score = [(EV Demand × 0.35) + (Cross-Industry Competition × 0.40) + (Geopolitical Risk × 0.25)] × (10/3)
```

Each dimension is scored 1.0 (low risk) to 3.0 (critical risk).
Final score is normalised to a 0–10 scale.

### Dimension Definitions

#### EV Demand (Weight: 0.35)
Reflects the rate of EV penetration growth and battery chemistry dependency on the specific material.
- Score 3.0: Material is essential for NMC/NCA chemistry in fast-growing EV markets; demand trajectory accelerating
- Score 2.0: Material used in multiple battery chemistries but partial LFP substitution occurring
- Score 1.0: Material not directly required for dominant EV battery chemistry in key markets

*PCA rationale:* EV Demand weight (0.35) reflects the exponential EV adoption variance — expected to be the primary loading factor when PCA is run on supply disruption time-series data.

#### Cross-Industry Competition (Weight: 0.40)
The number and scale of non-EV sectors competing for the same material supply pool. This is the primary Leontief contagion mechanism — the higher the cross-industry competition, the more sectors are simultaneously disrupted by a single supply shock.
- Score 3.0: Three or more major industrial sectors compete for the same supply pool simultaneously (e.g., nickel: EV + stainless steel + aerospace)
- Score 2.0: Two sectors with moderate competition
- Score 1.0: One primary sector with limited cross-industry demand

*This weight (0.40) is the highest because cross-sector demand competition is the primary contagion mechanism in the Leontief model. One supply restriction propagates to all competing sectors simultaneously.*

#### Geopolitical Risk (Weight: 0.25)
Supplier concentration (HHI-calculable from USGS data), history of export controls, and geopolitical relationship with India.
- Score 3.0: Single country controls >60% of global production or refining; documented export control history; adversarial geopolitical relationship
- Score 2.0: Two to three countries dominate; moderate concentration risk
- Score 1.0: Geographically distributed production; no significant export control history

### Risk Tier Classification
| Score | Tier | Meaning |
|-------|------|---------|
| ≥ 8.5 | 🔴 CRITICAL | Immediate policy and procurement action required |
| 7.0–8.4 | 🟠 HIGH | Active monitoring and diversification strategy required |
| 5.5–6.9 | 🟡 MEDIUM | Structured risk management recommended |
| < 5.5 | 🟢 LOW | Standard procurement risk management sufficient |

---

## 3. Methodology Limitations and Honest Disclosures

### What the Scores Are
- Expert-calibrated analytical judgements grounded in Leontief I-O economics
- Designed for compatibility with future PCA validation
- Directionally robust for strategic planning purposes

### What the Scores Are Not
- Regression-derived statistical outputs
- Commodity price forecasts
- Precise point estimates (they carry implicit uncertainty ranges)
- Validated through backtesting (backtesting is a 90-day target)

### Known Limitations
1. **India-specific I-O table not yet constructed** — current Leontief multipliers use OECD TiVA as proxy
2. **PCA not yet executed** — weights are expert-calibrated, not statistically derived
3. **UBO ownership data** — based on publicly available corporate ownership information; may not capture all recent ownership changes
4. **J&K lithium** — G3/G4 UNFC classification; no commercial extraction precedent for claystone deposits
5. **Chemistry shift lag** — NMC/LFP market share data has a 3–6 month reporting lag
6. **Export control events** — a structured database of past events for backtesting has not yet been compiled

---

## 4. Data Sources by Dimension

### EV Demand Data
| Source | Data Used | Tier |
|--------|-----------|------|
| IEA Global EV Outlook 2026 | EV sales by country, battery chemistry mix | A |
| ICCT Global EV Market Monitor 2025 | Market share by country, segment analysis | A |
| SIAM (India) | Monthly EV registrations by segment | A |
| ING Think — Nickel Capped by Surplus 2025 | NMC vs LFP chemistry split in China | A |

### Cross-Industry Competition Data
| Source | Data Used | Tier |
|--------|-----------|------|
| Stainless Steel World 2025 | Nickel demand split: stainless vs battery | A |
| ScienceDirect (2023) | Nickel superalloys in aerospace turbine blades | A |
| IEA Critical Minerals Outlook 2025 | Battery demand as % of total critical mineral demand | A |

### Geopolitical Risk Data
| Source | Data Used | Tier |
|--------|-----------|------|
| USGS Mineral Commodity Summaries 2025 | Production by country — HHI basis | A |
| Statranker / Investing News (2025) | Indonesia nickel dominance (67%+) | A |
| Takshashila Institution (2025) | China Oct 2024 export controls detail | A |
| IEEFA/ICRIER (2026) | India Variant A/B nickel trade dynamics | A |

---

## 5. UBO Risk Methodology

### Definition
**Ultimate Beneficiary Ownership Risk (UBO Risk):** The supply chain vulnerability created when the corporate entity that makes production, pricing, and allocation decisions for a critical industrial input is beneficially owned or operationally controlled by a foreign state-linked conglomerate — regardless of the geographic location of the physical asset or the national flag on the shipping certificate.

### Application Protocol
For each supply node in the framework:
1. Identify the geographic origin (country-of-origin certificate)
2. Identify the operating company
3. Research the beneficial ownership of the operating company
4. Identify the country of beneficial owner headquarters
5. Assess state-linkage of the beneficial owner (state-owned enterprise, state-influenced, or private)
6. Classify UBO Risk: Western / Mixed / Chinese / Russian / Other

### Current UBO Classifications

| Supply Node | Origin Country | Operating Entity | Beneficial Owner HQ | UBO Classification |
|-------------|---------------|-----------------|---------------------|-------------------|
| Indonesian HPAL plants | Indonesia | Tsingshan Holding / Huayou Cobalt | Wenzhou / Tongxiang, China | 🔴 Chinese |
| DRC Cobalt — Tenke Fungurume | DRC | CMOC Group | Beijing, China | 🔴 Chinese |
| DRC Cobalt — Kisanfu | DRC | CMOC Group | Beijing, China | 🔴 Chinese |
| DRC Cobalt — Mutanda | DRC | Glencore | Baar, Switzerland | 🟢 Western |
| Belgian NiSO₄ — Umicore Olen | Belgium | Umicore NV | Brussels, Belgium | 🟡 Mixed (feedstock: Russian/African) |
| Finnish NiSO₄ — Harjavalta | Finland | Norilsk Nickel Harjavalta | Moscow (Norilsk) | 🟠 Russian-linked |
| Australia BHP Nickel West | Australia | BHP Group | Melbourne, Australia | 🟢 Western |
| Australia TLEA (IGO/Tianqi) | Australia | Tianqi Lithium Energy Australia | Perth / Shenzhen | 🟡 Mixed (Tianqi = Chinese) |

---

## 6. pCAM Synthesis Chemistry — Technical Documentation

### Why This Matters for Supply Chain Analysis
India's domestic pCAM (Precursor Cathode Active Material) plants are cited as evidence of midstream localisation. This section documents why that claim requires qualification.

### The Chemistry
**Inputs:**
- NiSO₄·6H₂O (nickel sulphate hexahydrate) — dissolved in deionised water
- CoSO₄·7H₂O (cobalt sulphate heptahydrate)
- MnSO₄·H₂O (manganese sulphate monohydrate)
- NaOH solution (sodium hydroxide, precipitation agent)
- NH₄OH solution (ammonium hydroxide, chelating/morphology control agent)

**Process:**
Metal sulphate solution fed into a Continuous Stirred Tank Reactor (CSTR). NaOH dosed to raise pH to 11–12, causing co-precipitation of Ni(OH)₂, Co(OH)₂, and Mn(OH)₂ as a Mixed Hydroxide Precursor (MHP) particle. NH₄OH complexes with dissolved metal ions, controlling nucleation kinetics to produce uniform spherical secondary particles of 10–15 microns diameter (required for tap density and energy density targets).

**The strategic implication:**
The NaOH precipitation step increases bulk mass and volume of the product relative to the metal sulphate inputs. An Indian facility performing this step can claim domestic pCAM production. However, the NiSO₄, CoSO₄, and MnSO₄ inputs are:
- NiSO₄: 65%+ Belgium (Umicore), Japan, Finland — feedstock: Russian/African-Chinese
- CoSO₄: ~80% Chinese-processed DRC cobalt
- MnSO₄: ~60% Chinese sulphation of South African ore

The domestic value addition is the precipitation chemistry. The strategic value addition is limited — it resides in the metal sulphate inputs, not the precipitation step.

**Domestic inputs (potential):**
- NaOH: India has chlor-alkali industry (Reliance, Gujarat Alkalies, Tata Chemicals) — potentially domestic if battery-grade purity specifications are met
- NH₄OH: India has ammonia production (GSFC, IFFCO, Chambal Fertilisers) — potentially domestic subject to purity qualification

---

## 7. Chemistry Longevity Clause

This framework is an **Inflexible Infrastructure Dependency Matrix**, not a lithium or nickel calculator. The table below maps Chinese infrastructure dependency across chemistry variants:

| Chemistry | Precursor Synthesis | Sulphation China % | Cell Equipment China % | Dependency Status |
|-----------|--------------------|--------------------|----------------------|------------------|
| NMC | NaOH/NH₄OH CSTR | ~82% | ~87% | Full dependency |
| LFP | NaOH synthesis route | 0% (no Ni/Co) | ~85% | Partial — Ni/Co eliminated |
| Na-ion (layered oxide P2/O3) | NaOH/NH₄OH CSTR | ~68% | ~85% | Migrated — same bottleneck |
| Na-ion (PBA only) | Simple co-precipitation | 0% | ~70% | Reduced — bounded to ~160 Wh/kg |

**Conclusion:** LFP reduces but does not eliminate infrastructure dependency. Sodium-ion (layered oxide) migrates but does not escape it. Only a complete rebuild of midstream chemical processing infrastructure outside China — regardless of chemistry — resolves the structural chokepoint.

---

## 8. PCA Upgrade Pathway

### What PCA Would Do
Principal Component Analysis on a panel dataset (10 years × 6 materials × 4 dimensions) would:
1. Identify latent factors that explain the most variance in supply disruption outcomes
2. Calculate factor loadings to determine empirical weights for EV Demand, Cross-Industry, and Geopolitical dimensions
3. Replace the current expert-calibrated weights (0.35/0.40/0.25) with statistically derived weights
4. Enable statement: "PCA on 10-year supply disruption data identifies three latent factors explaining X% of variance"

### Required Variables
| Track | Variables | Source | Frequency |
|-------|-----------|--------|-----------|
| Price Volatility | Monthly price series, CV, max drawdown | LME, Fastmarkets, PVInsights | Monthly 2015–present |
| Supply Concentration | HHI by material by year | USGS Mineral Commodity Summaries | Annual 2015–2025 |
| India Import Dependence | Volume by material, source country share | DGCI&S, UN Comtrade | Annual + Quarterly |
| Refining Concentration | Processing share by country | IEA Critical Minerals Outlook | Annual 2018–2025 |
| Export Control Events | Dates, materials, duration, price impact | MOFCOM, ESDM, WTO | Event-driven |
| EV Chemistry Mix | NMC/LFP/Na-ion share by country | ICCT, BloombergNEF, SIAM | Quarterly |

### Timeline
- **30 days:** Data collection and clean DataFrame construction
- **90 days:** PCA execution, weight derivation, backtesting — CIIP v4.2
- **12 months:** Monte Carlo confidence intervals, network centrality — CIIP v5.0

---

## 9. Scenario Architecture

All 2030 projections are **Tier C** — strategic scenario assumptions, not econometric forecasts.

| Scenario | Key Assumptions | Battery $B | Solar $B | Total |
|----------|----------------|-----------|---------|-------|
| S1 — China Dominance | No domestic refining. PLI underdelivers. China controls 80%+ midstream. NMC dominant. | $23B | $30B | **$53B** |
| S2 — Moderate Localisation | Partial PLI success. 25 GWh domestic. J&K auction succeeds. LFP/NMC split. | $17B | $21B | **$38B** |
| S3 — Aggressive Refining | Adani Mundra + non-J&K Li refinery operational. AU/Chile partnerships. | $11B | $13B | **$24B** |
| S4 — Na-ion + Recycling | Na-ion commercialised for 2W/grid. LFP dominant. Recycling 20%+ recovery. | $8B | $11B | **$19B** |

---

*This methodology document is version-controlled alongside the framework. Updates to scoring weights, data sources, or analytical approaches will be documented here with version number and date.*

**Author:** Aditya V Sivaram Poduri
**Framework:** CIIP Battery Intelligence v4.1
**Date:** June 2026
