from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    regime_atual = Column(String, nullable=True)
    margem_lucro = Column(Float, nullable=True)

    simulacoes = relationship("Simulacao", back_populates="empresa")


class Simulacao(Base):
    __tablename__ = "simulacoes"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    faturamento = Column(Float, nullable=False)

    imposto_simples = Column(Float)
    imposto_presumido = Column(Float)
    imposto_real = Column(Float)

    melhor_regime = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    empresa = relationship("Empresa", back_populates="simulacoes")