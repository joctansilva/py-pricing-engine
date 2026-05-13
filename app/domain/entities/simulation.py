from dataclasses import dataclass


@dataclass
class SimulationInput:
    product_code: str
    session_id: dict
    params: dict


@dataclass
class SimulationResult:
    product_code: str
    base_premium: float
    final_premium: float
    breakdown: list[dict]
    duration_ms: float
    is_eligible: bool
    rejection_reasons: list[str]
