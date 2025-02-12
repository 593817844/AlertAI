from fastapi import FastAPI, Request
from typing import List, Dict, Optional,Any
from pydantic import BaseModel, Extra
from datetime import datetime

app = FastAPI()


record_data={}


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
    status: str
    labels: Dict[str, str]  # 存储标签，如 alertname、instance 等
    annotations: Dict[str, str]  # 存储注解，如 summary 等
    startsAt: str
    endsAt: Optional[str] = None  # endsAt 是可选的
    fingerprint: str
    duration: Optional[int] = None

@app.post("/alert")
# async def receive_alert(item: Dict[str, Any]):
async def receive_alert(data: WebhookData):
    print(f"输入原始数据\n{data}")
    for alert in data.alerts:
        if alert.status == "firing":
            record_data[alert.fingerprint]= RecordAlert(
                status=alert.status,
                labels=alert.labels,
                annotations=alert.annotations,
                startsAt=alert.startsAt,
                endsAt=None,
                fingerprint=alert.fingerprint,
                duration=None
                )
        elif alert.status == "resolved":
            if not record_data.get(alert.fingerprint):
                print("告警已恢复,但是找不到相应ID")
                return {"message": "告警已恢复,但是找不到相应ID"}
            record_data[alert.fingerprint].status = "resolved"
            record_data[alert.fingerprint].endsAt = alert.endsAt
            
            starts_at = datetime.fromisoformat(alert.startsAt[:-1])
            ends_at = datetime.fromisoformat(alert.endsAt[:-1])
            duration = (ends_at - starts_at).seconds
            
            record_data[alert.fingerprint].duration = duration
        else:
            print("输入格式不正确")
        print(f"记录数据打印\n{record_data}")


    return {"message": "Alert received successfully"}
