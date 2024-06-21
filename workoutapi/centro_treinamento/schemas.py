from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import Field,UUID4


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento",example="CT King",max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento",example="Rua x Quadra 2",max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento",example="Marcos",max_length=30)]

class CentroTrinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento",example="CT King",max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id:Annotated[UUID4,Field(description = "Identificador do centro de treinamento")]