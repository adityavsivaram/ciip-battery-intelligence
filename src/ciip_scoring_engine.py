"""
CIIP Battery Intelligence Framework — Core Scoring Engine
==========================================================
Cross-Industry Input Pressure (CIIP) Battery Index v4.1

Theoretical basis: Leontief Input-Output Economics (Nobel 1973)
Author: Aditya V Sivaram Poduri
Published: June 2026
Framework: India Supply Chain Signals

IMPORTANT: Scores are expert-calibrated analytical judgements grounded
in Leontief I-O economics. They are NOT regression-derived statistical
outputs. PCA validation is on the 90-day empirical upgrade roadmap.
"""

from dataclasses import dataclass, field
from typing import Optional
import json


# ── CONSTANTS ─────────────────────────────────────────────────────────────────

EV_WEIGHT     = 0.35   # Reflects exponential EV adoption variance
CROSS_WEIGHT  = 0.40   # Primary Leontief contagion mechanism (highest weight)
GEO_WEIGHT    = 0.25   # HHI-based production concentration
NORMALISE     = 10 / 3  # Normalises 1–3 scale to 0–10

CRITICAL_THRESHOLD = 8.5
HIGH_THRESHOLD     = 7.0
MEDIUM_THRESHOLD   = 5.5


# ── DATA CLASSES ──────────────────────────────────────────────────────────────

@dataclass
class CIIPScore:
    """Result of a CIIP scoring calculation."""
    material: str
    ev_demand: float
    cross_industry: float
    geopolitical: float
    score: float
    tier: str
    sectors: str
    conditionality: str
    data_confidence: str = "Tier B"  # Scores are expert-calibrated (Tier B)
    notes: str = ""

    def to_dict(self):
        return {
            "material": self.material,
            "ev_demand": self.ev_demand,
            "cross_industry": self.cross_industry,
            "geopolitical": self.geopolitical,
            "ciip_score": self.score,
            "tier": self.tier,
            "sectors": self.sectors,
            "conditionality": self.conditionality,
            "data_confidence": self.data_confidence,
            "notes": self.notes,
            "weights": {
                "ev": EV_WEIGHT,
                "cross_industry": CROSS_WEIGHT,
                "geopolitical": GEO_WEIGHT
            },
            "formula": f"({self.ev_demand}×{EV_WEIGHT} + {self.cross_industry}×{CROSS_WEIGHT} + {self.geopolitical}×{GEO_WEIGHT}) × {NORMALISE:.4f}"
        }

    def __str__(self):
        return (
            f"\n{'='*55}\n"
            f"  {self.material.upper()} — CIIP Score: {self.score:.1f}/10  [{self.tier}]\n"
            f"{'='*55}\n"
            f"  EV Demand:          {self.ev_demand:.1f}/3.0  (weight: {EV_WEIGHT})\n"
            f"  Cross-Industry:     {self.cross_industry:.1f}/3.0  (weight: {CROSS_WEIGHT})\n"
            f"  Geopolitical Risk:  {self.geopolitical:.1f}/3.0  (weight: {GEO_WEIGHT})\n"
            f"  Sectors:            {self.sectors}\n"
            f"  Conditionality:     {self.conditionality}\n"
            f"  Data confidence:    {self.data_confidence}\n"
            f"{'='*55}\n"
        )


# ── MASTER MATERIAL DATABASE ──────────────────────────────────────────────────

MATERIAL_DATABASE = {
    "nickel": {
        "ev_demand": 3.0,
        "cross_industry": 3.0,
        "geopolitical": 3.0,
        "sectors": "EV batteries (NMC) + stainless steel + aerospace turbine blades (Inconel superalloys)",
        "conditionality": (
            "Score conditional on NMC pathway remaining dominant in India. "
            "Falls to 6.8 under LFP dominance, 5.1 under Na-ion. "
            "Aerospace demand provides structural floor independent of EV chemistry — "
            "Inconel superalloys have no substitute above 1,000°C. "
            "Indonesia produces 67%+ of global output (not Australia/South America). "
            "UBO Risk: Indonesian HPAL plants are Chinese-owned (Tsingshan, Huayou Cobalt)."
        ),
        "notes": (
            "Nickel Variant A (NiO/Ni(OH)2/MHP): India sources 64.7% from Australia (IEEFA/ICRIER Tier A). "
            "Nickel Variant B (NiSO4): India sources 65%+ from Belgium/Umicore (IEEFA/ICRIER Tier A). "
            "Australia BHP Nickel West = genuine Western UBO. "
            "Indonesian component of Variant A = Chinese UBO despite Indonesian certificate."
        )
    },
    "lithium": {
        "ev_demand": 3.0,
        "cross_industry": 2.5,
        "geopolitical": 2.8,
        "sectors": "EV batteries + grid storage + consumer electronics",
        "conditionality": (
            "J&K reserve is G3/G4 UNFC — geological notation, not bankable reserve. "
            "Claystone extraction unproven at industrial scale globally. "
            "Minimum 13–20 years to battery-grade output from J&K. "
            "Recycling offset reduces score ~0.4 by 2030. "
            "Australia CMIN off-take (LiOH from Kemerton/TLEA) is the only genuine near-term de-risking. "
            "Export-reimport trap: spodumene $1,000/t vs LiOH-H2O $18,000/t if India mines without refining."
        ),
        "notes": "India imports 18,200t lithium 2025; 68% from China. India lithium refining: zero. (IEEFA/IndexBox Tier A)"
    },
    "polysilicon": {
        "ev_demand": 2.8,
        "cross_industry": 2.8,
        "geopolitical": 3.0,
        "sectors": "Solar PV + semiconductors + optoelectronics",
        "conditionality": (
            "Vietnam/Malaysia re-labelling keeps effective score elevated even as headline China share falls. "
            "Both countries source 85–95% polysilicon from China. "
            "Adani Mundra commissioning (Base Case 2029) reduces score to ~7.5. "
            "Structural electricity cost gap: India $0.09–0.11/kWh vs China $0.03–0.05/kWh. "
            "Siemens process requires 30–40 kWh/kg — creates ongoing competitiveness challenge."
        ),
        "notes": "China: 91% polysilicon, 97% wafers (IEA 2025 Tier A). India $7B solar imports FY2024."
    },
    "cobalt": {
        "ev_demand": 2.5,
        "cross_industry": 2.0,
        "geopolitical": 3.0,
        "sectors": "EV batteries (NMC) + aerospace superalloys + defence electronics",
        "conditionality": (
            "Dual chokepoint: DRC mines 70%+ globally, China refines 80% of cobalt sulphate. "
            "UBO Risk: CMOC (Chinese) owns Tenke Fungurume and Kisanfu — two of DRC's largest mines. "
            "Most sensitive material to recycling — hydromet recovery economics strongest for cobalt. "
            "2030 score could fall to ~7.0 with aggressive urban mining. "
            "LFP chemistry shift reduces cobalt demand — partially mitigating the risk."
        ),
        "notes": "India cobalt refining: 2,060t/yr — insufficient for battery-scale demand."
    },
    "graphite": {
        "ev_demand": 2.5,
        "cross_industry": 1.5,
        "geopolitical": 3.0,
        "sectors": "Battery anode (natural + synthetic) + steelmaking + nuclear moderator",
        "conditionality": (
            "China Oct 2024 export controls are a live escalation vector. "
            "Synthetic graphite from petroleum coke is a partial substitute but "
            "requires 3–5 year manufacturing build in India. "
            "No current anode-grade processing capacity in India. "
            "China controls ~85% of global anode-grade graphite processing."
        ),
        "notes": "China graphite export controls October 2024 (Takshashila 2025 Tier A)."
    },
    "manganese": {
        "ev_demand": 2.0,
        "cross_industry": 2.0,
        "geopolitical": 2.0,
        "sectors": "NMC batteries + steel alloys + fertiliser production (LMFP emerging)",
        "conditionality": (
            "South Africa (36%) and Gabon (16%) provide geographic diversification — lower concentration risk. "
            "China processes ~50% globally (vs 80%+ for nickel/cobalt). "
            "MEDIUM score reflects structurally lower concentration. "
            "Rising under LMFP (lithium manganese iron phosphate) chemistry adoption."
        ),
        "notes": "Most geographically diversified of the six materials. MEDIUM tier reflects lower chokepoint risk."
    }
}


# ── SCORING ENGINE ────────────────────────────────────────────────────────────

class CIIPScorer:
    """
    CIIP Battery Index Scoring Engine v4.1

    Usage:
        scorer = CIIPScorer()
        result = scorer.score("nickel")
        print(result)

        # Or score with custom values
        result = scorer.score_custom("test_material", ev=2.5, cross=2.0, geo=2.5)

        # Score all materials
        all_scores = scorer.score_all()
    """

    def __init__(self,
                 ev_weight: float = EV_WEIGHT,
                 cross_weight: float = CROSS_WEIGHT,
                 geo_weight: float = GEO_WEIGHT):
        self.ev_weight = ev_weight
        self.cross_weight = cross_weight
        self.geo_weight = geo_weight

        # Validate weights sum to 1.0
        total = ev_weight + cross_weight + geo_weight
        if abs(total - 1.0) > 0.001:
            raise ValueError(f"Weights must sum to 1.0. Current sum: {total:.3f}")

    def _calculate(self, ev: float, cross: float, geo: float) -> float:
        """Core CIIP formula."""
        return round(
            (ev * self.ev_weight + cross * self.cross_weight + geo * self.geo_weight) * NORMALISE,
            1
        )

    def _classify_tier(self, score: float) -> str:
        """Classify score into risk tier."""
        if score >= CRITICAL_THRESHOLD:
            return "CRITICAL"
        elif score >= HIGH_THRESHOLD:
            return "HIGH"
        elif score >= MEDIUM_THRESHOLD:
            return "MEDIUM"
        else:
            return "LOW"

    def score(self, material: str) -> CIIPScore:
        """
        Score a material using database values.

        Args:
            material: Material name (nickel, lithium, polysilicon, cobalt, graphite, manganese)

        Returns:
            CIIPScore dataclass with full scoring details
        """
        material_lower = material.lower()
        if material_lower not in MATERIAL_DATABASE:
            available = ", ".join(MATERIAL_DATABASE.keys())
            raise ValueError(f"Material '{material}' not found. Available: {available}")

        data = MATERIAL_DATABASE[material_lower]
        ev = data["ev_demand"]
        cross = data["cross_industry"]
        geo = data["geopolitical"]
        score = self._calculate(ev, cross, geo)
        tier = self._classify_tier(score)

        return CIIPScore(
            material=material.title(),
            ev_demand=ev,
            cross_industry=cross,
            geopolitical=geo,
            score=score,
            tier=tier,
            sectors=data["sectors"],
            conditionality=data["conditionality"],
            notes=data.get("notes", "")
        )

    def score_custom(self,
                     material: str,
                     ev: float,
                     cross: float,
                     geo: float,
                     sectors: str = "Custom",
                     conditionality: str = "Custom analysis") -> CIIPScore:
        """
        Score any material with custom dimension values.

        Args:
            material: Name of the material
            ev: EV Demand score (1.0 to 3.0)
            cross: Cross-Industry Competition score (1.0 to 3.0)
            geo: Geopolitical Risk score (1.0 to 3.0)
            sectors: Description of competing sectors
            conditionality: Conditionality notes

        Returns:
            CIIPScore dataclass
        """
        for name, val in [("ev", ev), ("cross", cross), ("geo", geo)]:
            if not 1.0 <= val <= 3.0:
                raise ValueError(f"Score '{name}' must be between 1.0 and 3.0. Got: {val}")

        score = self._calculate(ev, cross, geo)
        tier = self._classify_tier(score)

        return CIIPScore(
            material=material,
            ev_demand=ev,
            cross_industry=cross,
            geopolitical=geo,
            score=score,
            tier=tier,
            sectors=sectors,
            conditionality=conditionality,
            data_confidence="Tier B — Custom calibration"
        )

    def score_all(self) -> list:
        """Score all materials in the database, sorted by score descending."""
        results = [self.score(m) for m in MATERIAL_DATABASE.keys()]
        return sorted(results, key=lambda x: x.score, reverse=True)

    def summary_table(self) -> str:
        """Print a formatted summary table of all material scores."""
        scores = self.score_all()
        header = f"\n{'CIIP Battery Index v4.1 — All Material Scores':^65}"
        separator = "─" * 65
        row_fmt = "{:<15} {:>8} {:>12} {:>10} {:>10} {:>10}"

        lines = [header, separator,
                 row_fmt.format("Material", "CIIP Score", "Tier", "EV", "Cross-Ind", "Geo Risk"),
                 separator]

        for s in scores:
            lines.append(row_fmt.format(
                s.material,
                f"{s.score:.1f}/10",
                s.tier,
                f"{s.ev_demand:.1f}",
                f"{s.cross_industry:.1f}",
                f"{s.geopolitical:.1f}"
            ))

        lines.append(separator)
        lines.append(f"\nWeights: EV={self.ev_weight} | Cross-Industry={self.cross_weight} | Geopolitical={self.geo_weight}")
        lines.append("Note: Scores are expert-calibrated Tier B estimates. PCA validation on 90-day roadmap.")
        return "\n".join(lines)

    def export_json(self, filepath: Optional[str] = None) -> str:
        """Export all scores to JSON."""
        scores = self.score_all()
        data = {
            "framework": "CIIP Battery Intelligence v4.1",
            "author": "Aditya V Sivaram Poduri",
            "published": "June 2026",
            "methodology": "Expert-calibrated Leontief I-O basis. PCA validation pending.",
            "data_confidence_note": "All scores are Tier B — derived analytical estimates",
            "weights": {
                "ev_demand": self.ev_weight,
                "cross_industry": self.cross_weight,
                "geopolitical": self.geo_weight,
                "normalisation_factor": NORMALISE
            },
            "thresholds": {
                "CRITICAL": f">= {CRITICAL_THRESHOLD}",
                "HIGH": f">= {HIGH_THRESHOLD}",
                "MEDIUM": f">= {MEDIUM_THRESHOLD}",
                "LOW": f"< {MEDIUM_THRESHOLD}"
            },
            "scores": [s.to_dict() for s in scores]
        }
        json_str = json.dumps(data, indent=2)
        if filepath:
            with open(filepath, "w") as f:
                f.write(json_str)
            print(f"Scores exported to: {filepath}")
        return json_str


# ── LEONTIEF I-O MATRIX ───────────────────────────────────────────────────────

IO_MATRIX = {
    # material: {sector: dependency_coefficient}
    # Coefficient = import dependency (0.0 to 1.0)
    # >0.70 = critical chokepoint, 0.40-0.70 = high, 0.20-0.40 = moderate
    "nickel": {
        "ev_batteries": 0.85,
        "solar_pv": 0.05,
        "stainless_steel": 0.72,
        "aerospace": 0.68,
        "grid_storage": 0.45,
        "electronics": 0.12
    },
    "lithium": {
        "ev_batteries": 0.92,
        "solar_pv": 0.08,
        "stainless_steel": 0.03,
        "aerospace": 0.05,
        "grid_storage": 0.88,
        "electronics": 0.18
    },
    "polysilicon": {
        "ev_batteries": 0.04,
        "solar_pv": 0.95,
        "stainless_steel": 0.01,
        "aerospace": 0.02,
        "grid_storage": 0.12,
        "electronics": 0.35
    },
    "cobalt": {
        "ev_batteries": 0.78,
        "solar_pv": 0.02,
        "stainless_steel": 0.08,
        "aerospace": 0.52,
        "grid_storage": 0.65,
        "electronics": 0.22
    },
    "graphite": {
        "ev_batteries": 0.88,
        "solar_pv": 0.03,
        "stainless_steel": 0.02,
        "aerospace": 0.04,
        "grid_storage": 0.82,
        "electronics": 0.15
    },
    "manganese": {
        "ev_batteries": 0.42,
        "solar_pv": 0.02,
        "stainless_steel": 0.38,
        "aerospace": 0.15,
        "grid_storage": 0.35,
        "electronics": 0.06
    }
}

LEONTIEF_MULTIPLIERS = {
    # Estimated output multipliers (Tier B — OECD TiVA proxy for India)
    # Meaning: $1 of supply disruption generates $X of downstream industrial output impact
    "nickel": 2.8,
    "polysilicon": 2.6,
    "lithium": 2.4,
    "cobalt": 1.9,
    "graphite": 1.7,
    "manganese": 1.4
}


def contagion_impact(material: str, disruption_value_usd_m: float) -> dict:
    """
    Calculate downstream industrial impact of a supply disruption
    using Leontief output multipliers.

    Args:
        material: Critical material affected
        disruption_value_usd_m: Value of supply disruption in USD million

    Returns:
        Dictionary of downstream impacts by sector
    """
    material_lower = material.lower()
    if material_lower not in IO_MATRIX:
        raise ValueError(f"Material '{material}' not in I-O matrix.")

    multiplier = LEONTIEF_MULTIPLIERS.get(material_lower, 1.5)
    total_downstream = disruption_value_usd_m * multiplier
    coefficients = IO_MATRIX[material_lower]

    sector_impacts = {}
    for sector, coeff in coefficients.items():
        if coeff >= 0.20:
            impact = disruption_value_usd_m * coeff * multiplier
            sector_impacts[sector] = {
                "dependency_coefficient": coeff,
                "estimated_impact_usd_m": round(impact, 1),
                "severity": "CRITICAL" if coeff >= 0.70 else ("HIGH" if coeff >= 0.40 else "MODERATE")
            }

    return {
        "material": material,
        "disruption_value_usd_m": disruption_value_usd_m,
        "leontief_multiplier": multiplier,
        "total_downstream_impact_usd_m": round(total_downstream, 1),
        "sector_impacts": sector_impacts,
        "methodology_note": "Tier B — OECD TiVA proxy. India-specific I-O table on 12-month build roadmap."
    }


# ── SCENARIO SIMULATOR ────────────────────────────────────────────────────────

SCENARIOS = {
    "S1_china_dominance": {
        "name": "S1 — China Dominance Continues",
        "description": "No domestic refining. PLI underdelivers. China controls 80%+ midstream. NMC dominant.",
        "battery_imports_2030_bn": 23,
        "solar_imports_2030_bn": 30,
        "combined_2030_bn": 53,
        "india_cell_capacity_gwh": 5,
        "li_refining": "Near zero",
        "china_battery_share": "80%+",
        "nickel_ciip_adjusted": 10.0,
        "tier": "CRITICAL"
    },
    "S2_moderate": {
        "name": "S2 — Moderate Localisation",
        "description": "Partial PLI success. 25 GWh domestic. J&K auction succeeds (non-J&K feedstock refinery). LFP/NMC split.",
        "battery_imports_2030_bn": 17,
        "solar_imports_2030_bn": 21,
        "combined_2030_bn": 38,
        "india_cell_capacity_gwh": 25,
        "li_refining": "Partial",
        "china_battery_share": "55–65%",
        "nickel_ciip_adjusted": 8.8,
        "tier": "HIGH"
    },
    "S3_aggressive_refining": {
        "name": "S3 — Aggressive Refining Push",
        "description": "Adani Mundra + J&K operational. Aggressive AU/Chile partnerships. Some refining independence.",
        "battery_imports_2030_bn": 11,
        "solar_imports_2030_bn": 13,
        "combined_2030_bn": 24,
        "india_cell_capacity_gwh": 60,
        "li_refining": "Significant",
        "china_battery_share": "35–45%",
        "nickel_ciip_adjusted": 7.5,
        "tier": "HIGH"
    },
    "S4_sodium_recycling": {
        "name": "S4 — Sodium-Ion + Recycling",
        "description": "Na-ion commercialised for 2W/grid. LFP dominant. Recycling at 20%+ recovery. NMC niche only.",
        "battery_imports_2030_bn": 8,
        "solar_imports_2030_bn": 11,
        "combined_2030_bn": 19,
        "india_cell_capacity_gwh": 40,
        "li_refining": "Moderate",
        "china_battery_share": "30–40%",
        "nickel_ciip_adjusted": 5.5,
        "tier": "MEDIUM"
    }
}


def run_scenarios() -> dict:
    """Return full scenario comparison."""
    return {
        "framework": "CIIP Battery v4.1 Scenario Architecture",
        "note": "All projections are Tier C — strategic scenario assumptions, NOT econometric forecasts. Cite with scenario label.",
        "oil_import_fy25_bn": 116.4,
        "oil_import_source": "IEEFA March 2026 (Tier A)",
        "scenarios": SCENARIOS
    }


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*65)
    print("  CIIP Battery Intelligence Framework v4.1")
    print("  India's Green Import Trap — Scoring Engine")
    print("  Author: Aditya V Sivaram Poduri")
    print("="*65)

    scorer = CIIPScorer()

    # Print summary table
    print(scorer.summary_table())

    # Detailed score for nickel
    print("\n─── Detailed Score: Nickel ───")
    nickel = scorer.score("nickel")
    print(nickel)

    # Contagion analysis
    print("\n─── Contagion Analysis: Indonesia Nickel Quota -20% ───")
    impact = contagion_impact("nickel", disruption_value_usd_m=500)
    print(f"\nTotal downstream impact: ${impact['total_downstream_impact_usd_m']}M")
    print(f"Leontief multiplier: {impact['leontief_multiplier']}×")
    print("\nSector impacts:")
    for sector, data in impact['sector_impacts'].items():
        print(f"  {sector:<20} Coeff: {data['dependency_coefficient']:.2f}  "
              f"Impact: ${data['estimated_impact_usd_m']}M  [{data['severity']}]")

    # Export to JSON
    print("\n─── Exporting scores to JSON ───")
    scorer.export_json("data/processed/ciip_scores_master.json")
    print("\n✓ Scoring engine complete.")
