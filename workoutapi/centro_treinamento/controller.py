from uuid import uuid4
from centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from centro_treinamento.models import CentroTreinamentoModel
from atleta.models import AtletaModel
from contrib.dependencies import DatabaseDependency
from fastapi import APIRouter, Body, HTTPException,status
from sqlalchemy.future import select
from pydantic import UUID4

router = APIRouter()

@router.post(
        '/',
        summary="Criar um novo centro de treinamento",
        status_code = status.HTTP_201_CREATED,
        response_model=CentroTreinamentoOut
        )
async def post(
    db_session: DatabaseDependency,
    centro_treinamento_in:CentroTreinamentoIn = Body(...)
    )->CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(),**centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()
    return centro_treinamento_out


@router.get(
        '/',
        summary="Consultar todas os centros de treinamentos",
        status_code = status.HTTP_200_OK,
        response_model=list[CentroTreinamentoOut]
        )
async def query( db_session: DatabaseDependency )->list[CentroTreinamentoOut]:
    centro_treinamento_out: list[CentroTreinamentoOut]=(await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return centro_treinamento_out

@router.get(
        '/{id}',
        summary="Consultar uma centro de treinamento pelo id",
        status_code = status.HTTP_200_OK,
        response_model=CentroTreinamentoOut
        )
async def query(id:UUID4, db_session: DatabaseDependency )->CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut=(await db_session.execute(select(CentroTreinamentoModel).filter_by(id = id))
                             ).scalars().first()
    
    if not centro_treinamento_out:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail =  f'Centro de treinamento nao encontrado {id}'  
        )

    return centro_treinamento_out

  