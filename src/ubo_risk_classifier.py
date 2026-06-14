"""
CIIP Battery Intelligence Framework — UBO Risk Classifier
==========================================================
Ultimate Beneficiary Ownership Risk Analysis Module

This module implements the UBO Risk methodology introduced in CIIP v4.0.
It corrects the country-of-origin misclassification problem in standard
supply chain risk analysis.

DEFINITION:
UBO Risk = The supply chain vulnerability created when the corporate entity
that makes production, pricing, and allocation decisions for a critical
industrial input is beneficially owned or operationally controlled by a
foreign state-linked conglomerate — regardless of the geographic location
of the physical asset or the national flag on the shipping certificate.

Author: Aditya V Sivaram Poduri
Published: June 2026
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class UBOProfile:
    """UBO Risk profile for a supply node."""
    node_name: str
    origin_country: str
    operating_entity: str
    beneficial_owner: str
    beneficial_owner_hq: str
    state_linkage: str          # "state-owned" / "state-influenced" / "private"
    ubo_nationality: str
    ubo_classification: str     # "WESTERN" / "MIXED" / "CHINESE" / "RUSSIAN" / "OTHER"
    risk_mechanism: str
    verdict: str
    source_note: str = ""

    @property
    def flag_mismatch(self) -> bool:
        """Returns True if UBO nationality differs from origin country nationality."""
        return self.origin_country.lower() != self.ubo_nationality.lower()

    def __str__(self):
        mismatch_warn = " ⚠ FLAG MISMATCH" if self.flag_mismatch else " ✓ Aligned"
        return (
            f"\n{'─'*60}\n"
            f"  Node:              {self.node_name}\n"
            f"  Origin Country:    {self.origin_country}{mismatch_warn}\n"
            f"  Operating Entity:  {self.operating_entity}\n"
            f"  Beneficial Owner:  {self.beneficial_owner}\n"
            f"  Owner HQ:          {self.beneficial_owner_hq}\n"
            f"  State Linkage:     {self.state_linkage}\n"
            f"  UBO Nationality:   {self.ubo_nationality}\n"
            f"  UBO Classification:{self.ubo_classification}\n"
            f"  Risk Mechanism:    {self.risk_mechanism}\n"
            f"  Verdict:           {self.verdict}\n"
            f"{'─'*60}"
        )


# ── UBO DATABASE ──────────────────────────────────────────────────────────────

UBO_DATABASE = {
    "indonesia_hpal_tsingshan": UBOProfile(
        node_name="Indonesian HPAL Plants (Tsingshan)",
        origin_country="Indonesia",
        operating_entity="Tsingshan Holding Group",
        beneficial_owner="Tsingshan Holding Group",
        beneficial_owner_hq="Wenzhou, Zhejiang, China",
        state_linkage="state-influenced",
        ubo_nationality="China",
        ubo_classification="CHINESE",
        risk_mechanism=(
            "MHP production allocation decision (sell to India or redirect to Chinese "
            "cathode precursor plants) is made in Wenzhou, not Jakarta. "
            "This is a corporate decision, not a government policy — "
            "it does not appear in export control notifications."
        ),
        verdict=(
            "Country-of-origin certificate: Indonesia. "
            "UBO Risk nationality: China. "
            "The diversification is geographic. The control is Chinese."
        ),
        source_note="Tsingshan Holding Group HPAL operations in Sulawesi and Maluku, Indonesia."
    ),

    "indonesia_hpal_huayou": UBOProfile(
        node_name="Indonesian HPAL Plants (Huayou Cobalt)",
        origin_country="Indonesia",
        operating_entity="Huayou Cobalt",
        beneficial_owner="Huayou Cobalt Co. Ltd.",
        beneficial_owner_hq="Tongxiang, Zhejiang, China",
        state_linkage="state-influenced",
        ubo_nationality="China",
        ubo_classification="CHINESE",
        risk_mechanism=(
            "Huayou Cobalt operates HPAL plants producing MHP in Indonesia. "
            "Production allocation follows Chinese domestic demand priorities. "
            "73%+ stake in some Indonesian EV processing ventures."
        ),
        verdict=(
            "Same structure as Tsingshan: Indonesian geography, Chinese beneficial ownership. "
            "India's Variant A nickel sourced from Indonesian HPAL = Chinese UBO Risk."
        ),
        source_note="Huayou Cobalt Indonesian operations. LKY School 2025 (Tier A)."
    ),

    "belgium_umicore_niso4": UBOProfile(
        node_name="Belgian NiSO4 — Umicore Olen",
        origin_country="Belgium",
        operating_entity="Umicore NV",
        beneficial_owner="Umicore NV (publicly listed)",
        beneficial_owner_hq="Brussels, Belgium",
        state_linkage="private",
        ubo_nationality="Belgium",
        ubo_classification="MIXED",
        risk_mechanism=(
            "Umicore is genuinely Belgian — real first-order corporate diversification. "
            "However, NiSO4 feedstock includes Class I nickel from Norilsk-linked operations "
            "and African mines with Chinese concession ownership (CMOC, Huayou). "
            "If upstream feedstock is disrupted (Russian sanctions, African instability), "
            "Belgian NiSO4 output for export contracts drops."
        ),
        verdict=(
            "First-order corporate diversification: real. "
            "Second-order feedstock UBO exposure: Russian and partially Chinese. "
            "Mitigation: contractual provenance clauses requiring non-Russian, "
            "non-Chinese-UBO feedstock percentage minimum."
        ),
        source_note="IEEFA/ICRIER trade data (Tier A). Umicore 2025 Annual Report."
    ),

    "finland_norilsk_harjavalta": UBOProfile(
        node_name="Finnish NiSO4 — Norilsk Harjavalta",
        origin_country="Finland",
        operating_entity="Norilsk Nickel Harjavalta Oy",
        beneficial_owner="MMC Norilsk Nickel",
        beneficial_owner_hq="Moscow, Russia",
        state_linkage="state-influenced",
        ubo_nationality="Russia",
        ubo_classification="RUSSIAN",
        risk_mechanism=(
            "Norilsk Nickel holds significant stake in Harjavalta operations. "
            "Post-2022 sanctions created banking/shipping/insurance friction. "
            "Finnish facility location provides EU regulatory protection but "
            "feedstock and ownership remain Russian-linked."
        ),
        verdict=(
            "Origin certificate: Finland (EU). "
            "UBO Risk: Russian-linked. "
            "Subject to escalating sanctions risk and feedstock disruption risk."
        ),
        source_note="IEEFA/ICRIER Tier A. Norilsk Nickel corporate disclosures."
    ),

    "drc_cobalt_cmoc_tenke": UBOProfile(
        node_name="DRC Cobalt — Tenke Fungurume Mine",
        origin_country="Democratic Republic of Congo",
        operating_entity="CMOC Group",
        beneficial_owner="CMOC Group Limited",
        beneficial_owner_hq="Beijing, China",
        state_linkage="state-owned",  # CMOC has significant state ownership
        ubo_nationality="China",
        ubo_classification="CHINESE",
        risk_mechanism=(
            "CMOC acquired Tenke Fungurume from Freeport-McMoRan in 2016. "
            "One of DRC's largest cobalt-copper mines. "
            "Cobalt sulphate production direction follows Chinese cathode industry demand. "
            "DRC political instability and CMOC corporate decisions combine as dual risk vectors."
        ),
        verdict=(
            "Geographic origin: DRC. "
            "Beneficial owner: Chinese state-linked. "
            "India's CoSO4 imports trace back to Chinese-owned DRC production."
        ),
        source_note="CMOC Group corporate disclosure. IEA Critical Minerals 2025 (Tier A)."
    ),

    "drc_cobalt_cmoc_kisanfu": UBOProfile(
        node_name="DRC Cobalt — Kisanfu Mine",
        origin_country="Democratic Republic of Congo",
        operating_entity="CMOC Group",
        beneficial_owner="CMOC Group Limited",
        beneficial_owner_hq="Beijing, China",
        state_linkage="state-owned",
        ubo_nationality="China",
        ubo_classification="CHINESE",
        risk_mechanism=(
            "CMOC acquired Kisanfu (formerly Freeport Cobalt) in 2020. "
            "High-grade cobalt deposit. "
            "Both Tenke and Kisanfu under CMOC = Chinese control of DRC's two largest cobalt mines."
        ),
        verdict="Same UBO structure as Tenke Fungurume. Chinese beneficial ownership of DRC assets.",
        source_note="CMOC Group corporate disclosure."
    ),

    "australia_bhp_nickel_west": UBOProfile(
        node_name="Australia — BHP Nickel West",
        origin_country="Australia",
        operating_entity="BHP Nickel West",
        beneficial_owner="BHP Group Limited",
        beneficial_owner_hq="Melbourne, Australia",
        state_linkage="private",
        ubo_nationality="Australia",
        ubo_classification="WESTERN",
        risk_mechanism=(
            "Commercial allocation — no state-directed production redirection. "
            "Subject to commercial market pricing and BHP corporate strategy. "
            "BHP paused Nickel West green hub in mid-2024 due to nickel price pressure. "
            "Risk: production curtailment under low-price conditions, not geopolitical restriction."
        ),
        verdict=(
            "Genuine Western UBO. "
            "The benchmark for true supply chain independence. "
            "India-Australia CMIN partnership off-take is the recommended strategy."
        ),
        source_note="BHP Nickel West operations, Western Australia. USGS 2025 (Tier A)."
    ),
}


# ── UBO RISK CLASSIFIER ───────────────────────────────────────────────────────

class UBORiskClassifier:
    """
    UBO Risk Classification Engine

    Usage:
        classifier = UBORiskClassifier()

        # Get profile for a specific node
        profile = classifier.get_profile("australia_bhp_nickel_west")
        print(profile)

        # Get all Chinese UBO nodes
        chinese_nodes = classifier.filter_by_ubo("CHINESE")

        # Analyse India's nickel supply chain
        analysis = classifier.india_nickel_ubo_analysis()
    """

    def __init__(self):
        self.database = UBO_DATABASE

    def get_profile(self, node_key: str) -> UBOProfile:
        """Get UBO profile for a specific supply node."""
        if node_key not in self.database:
            available = "\n  ".join(self.database.keys())
            raise ValueError(f"Node '{node_key}' not found.\nAvailable nodes:\n  {available}")
        return self.database[node_key]

    def filter_by_ubo(self, ubo_classification: str) -> list:
        """Filter nodes by UBO classification (CHINESE, WESTERN, MIXED, RUSSIAN)."""
        return [p for p in self.database.values()
                if p.ubo_classification == ubo_classification.upper()]

    def get_flag_mismatches(self) -> list:
        """Return all nodes where origin country ≠ UBO nationality — the core UBO risk cases."""
        return [p for p in self.database.values() if p.flag_mismatch]

    def india_nickel_ubo_analysis(self) -> dict:
        """
        Full UBO analysis of India's nickel supply chain.
        Based on IEEFA/ICRIER trade data (Tier A).
        """
        return {
            "framework": "India Nickel Supply Chain — UBO Risk Analysis",
            "data_source": "IEEFA/ICRIER 2026 (Tier A)",
            "variant_a_nickel_oxides_hydroxides": {
                "description": "Nickel Oxides and Hydroxides / Mixed Hydroxide Precipitate (MHP)",
                "india_import_share": {
                    "Australia (BHP)": "64.7% — UBO: Western (GENUINE DIVERSIFICATION)",
                    "Indonesia (Tsingshan/Huayou HPAL)": "~28% — UBO: Chinese (HIDDEN RISK)",
                    "Other": "~7.3%"
                },
                "effective_chinese_ubo_exposure": "~28% of Variant A despite Indonesian certificate",
                "key_insight": (
                    "Australia 64.7% appears to be strong diversification. "
                    "The Indonesian component is Chinese-HPAL-owned — its 'Indonesian' label "
                    "survives a country-of-origin audit and fails a UBO audit."
                )
            },
            "variant_b_nickel_sulphate": {
                "description": "Battery-grade NiSO4·6H2O",
                "india_import_share": {
                    "Belgium/Umicore": "65%+ — UBO: Belgian (first-order genuine), feedstock: Russian/African-Chinese",
                    "Japan": "~18% — partial Chinese upstream exposure",
                    "Finland/Norilsk Harjavalta": "~10% — UBO: Russian-linked",
                    "Other": "~7%"
                },
                "key_insight": (
                    "Belgium sources provide genuine corporate diversification from China. "
                    "Feedstock UBO risk: Umicore's inputs include Norilsk-linked and "
                    "African mines with Chinese concessions. "
                    "Mitigation: contractual provenance disclosure clauses."
                )
            },
            "policy_implication": (
                "India's nickel supply chain diversification survives a country-of-origin audit "
                "and partially fails a UBO audit. True diversification requires "
                "BHP Nickel West MHP off-take (genuinely Western UBO) + "
                "domestic NiSO4 sulphation capacity (which India currently has zero of) + "
                "contractual feedstock provenance clauses for Belgian NiSO4 supply."
            )
        }

    def print_all_profiles(self):
        """Print all UBO profiles in the database."""
        print("\n" + "="*60)
        print("  CIIP Battery Intelligence v4.1 — UBO Risk Database")
        print("="*60)
        for key, profile in self.database.items():
            print(profile)

    def ubo_risk_summary(self) -> str:
        """Summary table of UBO classifications."""
        lines = [
            "\n" + "─"*70,
            f"  {'Node':<35} {'Origin':<12} {'UBO Classification':<20}",
            "─"*70
        ]
        for p in self.database.values():
            mismatch = " ⚠" if p.flag_mismatch else " ✓"
            lines.append(
                f"  {p.node_name:<35} {p.origin_country:<12} {p.ubo_classification:<20}{mismatch}"
            )
        lines.append("─"*70)
        lines.append("  ⚠ = Flag mismatch (origin ≠ UBO nationality)  ✓ = Aligned")
        lines.append(
            f"\n  Chinese UBO nodes: {len(self.filter_by_ubo('CHINESE'))}  "
            f"Western: {len(self.filter_by_ubo('WESTERN'))}  "
            f"Mixed: {len(self.filter_by_ubo('MIXED'))}  "
            f"Russian: {len(self.filter_by_ubo('RUSSIAN'))}"
        )
        return "\n".join(lines)


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    classifier = UBORiskClassifier()

    print("\n" + "="*65)
    print("  UBO Risk Classifier — CIIP Battery Intelligence v4.1")
    print("="*65)

    # Summary table
    print(classifier.ubo_risk_summary())

    # Flag mismatches
    print("\n─── Flag Mismatch Cases (Origin ≠ UBO Nationality) ───")
    mismatches = classifier.get_flag_mismatches()
    for p in mismatches:
        print(f"\n  {p.node_name}")
        print(f"  Origin: {p.origin_country}  |  UBO: {p.ubo_nationality} ({p.ubo_classification})")
        print(f"  Verdict: {p.verdict}")

    # India nickel analysis
    print("\n─── India Nickel Supply Chain — Full UBO Analysis ───")
    analysis = classifier.india_nickel_ubo_analysis()
    print(f"\nVariant A (Nickel Oxides/Hydroxides):")
    for k, v in analysis["variant_a_nickel_oxides_hydroxides"]["india_import_share"].items():
        print(f"  {k}: {v}")
    print(f"\nVariant B (Nickel Sulphate):")
    for k, v in analysis["variant_b_nickel_sulphate"]["india_import_share"].items():
        print(f"  {k}: {v}")
    print(f"\nPolicy Implication:\n  {analysis['policy_implication']}")
