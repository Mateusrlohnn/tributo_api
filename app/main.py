from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
import logging

from .database import engine, get_db
from .models import Base
from . import models, schemas
from .services import comparar_regimes

app = FastAPI()

Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"status": "API rodando"}

@app.post("/empresas", response_model=schemas.EmpresaResponse)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):

    nova_empresa = models.Empresa(
        nome=empresa.nome,
        cnpj=empresa.cnpj,
        regime_atual=empresa.regime_atual,
        margem_lucro=empresa.margem_lucro
    )

    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)

    logger.info(f"Empresa criada: {nova_empresa.id}")

    return nova_empresa
    
@app.get("/empresas", response_model=list[schemas.EmpresaResponse])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()


@app.post("/simular", response_model=schemas.SimulacaoResponse)
def simular(
    simulacao: schemas.SimulacaoCreate,
    db: Session = Depends(get_db)
):

    empresa = db.query(models.Empresa).filter(
        models.Empresa.id == simulacao.empresa_id
    ).first()

    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    simples, presumido, real, melhor = comparar_regimes(
        simulacao.faturamento,
        empresa.margem_lucro or 0.15
    )

    nova_simulacao = models.Simulacao(
        empresa_id=simulacao.empresa_id,
        faturamento=simulacao.faturamento,
        imposto_simples=simples,
        imposto_presumido=presumido,
        imposto_real=real,
        melhor_regime=melhor
    )

    db.add(nova_simulacao)
    db.commit()
    db.refresh(nova_simulacao)

    logger.info(f"Simulação criada para empresa {empresa.id}")

    return nova_simulacao

@app.get("/empresas/{empresa_id}/total-impostos")
def total_impostos(empresa_id: int, db: Session = Depends(get_db)):

    resultado = db.query(
        func.sum(models.Simulacao.imposto_simples),
        func.sum(models.Simulacao.imposto_presumido),
        func.sum(models.Simulacao.imposto_real)
    ).filter(
        models.Simulacao.empresa_id == empresa_id
    ).first()

    if not resultado:
        raise HTTPException(status_code=404, detail="Nenhuma simulação encontrada")

    return {
        "total_simples": resultado[0] or 0,
        "total_presumido": resultado[1] or 0,
        "total_real": resultado[2] or 0
    }