from datetime import datetime
from pydantic import BaseModel


class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    regime_atual: str | None = None
    margem_lucro: float | None = None


class EmpresaResponse(BaseModel):
    id: int
    nome: str
    cnpj: str
    regime_atual: str | None
    margem_lucro: float | None

    class Config:
        from_attributes = True


class SimulacaoCreate(BaseModel):
    empresa_id: int
    faturamento: float


class SimulacaoResponse(BaseModel):
    id: int
    empresa_id: int
    faturamento: float
    imposto_simples: float
    imposto_presumido: float
    imposto_real: float
    melhor_regime: str
    created_at: datetime

    class Config:
        from_attributes = True