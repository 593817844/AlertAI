from pydantic import BaseModel, fields, model_validator,Extra
from typing import List, Dict, Optional,Any
import settings

# 定义单个告警的模型
class SystemCreate(BaseModel):
    project: str
    architecture: str

    class Config:
        extra = Extra.ignore  # 忽略多余字段
        
class SystemResponse(BaseModel):
    id: int
    project: str
    architecture: str

    class Config:
        extra = Extra.ignore  # 忽略多余字段