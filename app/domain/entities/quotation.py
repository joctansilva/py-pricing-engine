from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class QuotationStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CONTRACTED = "CONTRACTED"
    CANCELLED = "CANCELLED"


@dataclass
class RuleApplication:
    rule_type: str
    rule_name: str
    value: float
    value_type: str
    effect: str


@dataclass
class Quotation:
    id: str
    quotation_code: str
    product_code: str
    customer_data: dict
    input_params: dict
    breakdown: list[RuleApplication]
    base_premium: float
    final_premium: float
    status: QuotationStatus
    valid_until: datetime
    created_at: datetime
