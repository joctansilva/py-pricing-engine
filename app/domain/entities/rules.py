from dataclasses import dataclass
from datetime import date
from typing import Optional
from enum import Enum


class RuleType(str, Enum):
    TAXA_BASE = "TAXA_BASE"
    DESCONTO_CAMPANHA = "DESCONTO_CAMPANHA"
    COEF_ETARIO_VIDA = "COEF_ETARIO_VIDA"
    COEF_GENERO = "COEF_GENERO"
    COEF_PROFISSAO = "COEF_PROFISSAO"
    COEF_FUMANTE = "COEF_FUMANTE"
    COEF_IMC = "COEF_IMC"
    FATOR_COBERTURA_VIDA = "FATOR_COBERTURA_VIDA"
    TAXA_BASE_AUTO = "TAXA_BASE_AUTO"
    FATOR_REGIONAL = "FATOR_REGIONAL"
    FATOR_CONDUTOR = "FATOR_CONDUTOR"
    FATOR_USO = "FATOR_USO"
    DESCONTO_BONUS = "DESCONTO_BONUS"
    FATOR_FRANQUIA = "FATOR_FRANQUIA"
    FATOR_ANTIGUIDADE = "FATOR_ANTIGUIDADE"
    VALOR_BASE_SAUDE = "VALOR_BASE_SAUDE"
    FATOR_ABRANGENCIA = "FATOR_ABRANGENCIA"
    FATOR_ACOMODACAO = "FATOR_ACOMODACAO"
    FATOR_COBERTURA_SAUDE = "FATOR_COBERTURA_SAUDE"
    DESCONTO_GRUPO = "DESCONTO_GRUPO"
    FATOR_ANS = "FATOR_ANS"


class ValueType(str, Enum):
    MULTIPLIER = "MULTIPLIER"
    PERCENTAGE = "PERCENTAGE"
    FIXED_AMOUNT = "FIXED_AMOUNT"


@dataclass
class PricingRule:
    id: str
    product_code: str
    rule_type: RuleType
    rule_name: str
    conditions: dict
    value: float
    value_type: ValueType
    priority: int
    valid_from: date
    valid_until: Optional[date]
    is_active: bool = True

    def is_valid_on(self, reference_date: date) -> bool:
        if not self.is_active:
            return False
        if reference_date < self.valid_from:
            return False
        if self.valid_until and reference_date > self.valid_until:
            return False
        return True
