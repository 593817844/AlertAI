from pydantic import BaseModel, fields, model_validator,Extra
from typing import List, Dict, Optional,Any
import settings

# 定义单个告警的模型
class Alert(BaseModel):
    status: str
    labels: Dict[str, str]  # 存储标签，如 alertname、instance 等
    annotations: Dict[str, str]  # 存储注解，如 summary 等
    startsAt: str
    endsAt: Optional[str] = None  # endsAt 是可选的
    generatorURL: str  # 添加 generatorURL 字段
    fingerprint: str

    class Config:
        extra = Extra.ignore  # 忽略多余字段


# 定义接收到的 Webhook 数据结构
class WebhookData(BaseModel):
    receiver: str
    status: str
    alerts: List[Alert]  # 多个告警
    groupLabels: Dict[str, str]
    commonLabels: Dict[str, str]
    commonAnnotations: Dict[str, str]
    externalURL: str
    version: str
    groupKey: str
    truncatedAlerts: int

    class Config:
        extra = Extra.ignore  # 忽略多余字段
        
class RecordAlert(BaseModel):
    id: str
    status: str
    labels: Dict[str, str]  # 存储标签，如 alertname、instance 等
    annotations: Dict[str, str]  # 存储注解，如 summary 等
    startsAt: str
    endsAt: Optional[str] = None  # endsAt 是可选的
    fingerprint: str
    duration: Optional[int] = None

    class Config:
        orm_mode = True  # 允许从 ORM 对象中读取数据
