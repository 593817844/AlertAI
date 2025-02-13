from fastapi import APIRouter
from . import scheams, models
from utils import logs
import os

logger = logs.getLogger(os.environ.get('APP_NAME'))

app = APIRouter()

@app.post("/system/",response_model=scheams.SystemResponse)
async def creat_systeminfo(s: scheams.SystemCreate):
    system = await models.SystemInfo.create(**s.dict())
    return scheams.SystemResponse(id=system.id,project=system.project,architecture=system.architecture)

