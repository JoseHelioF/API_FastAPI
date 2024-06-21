from typing import Annotated
from configs.database import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


DatabaseDependency = Annotated[AsyncSession,Depends(get_session)]