from fastapi import APIRouter
from . import scheams, models
from datetime import datetime
from utils import logs
import os
from typing import List
logger = logs.getLogger(os.environ.get('APP_NAME'))

app = APIRouter()

def generate_unique_id(var1, var2):
    return abs(hash((var1, var2))) 

@app.post("/alert")
# async def receive_alert(item: Dict[str, Any]):
async def receive_alert(data: scheams.WebhookData):
    try:
        print(f"输入原始数据\n{data}")
        logger.info(f"输入原始数据\n{data}")
        for alert in data.alerts:
            starts_at = datetime.fromisoformat(alert.startsAt[:-1])
            id = generate_unique_id(alert.fingerprint,alert.startsAt)
            if alert.status == "firing":
                await models.Alert.create(
                    id=id,
                    status=alert.status,
                    labels=alert.labels,
                    annotations=alert.annotations,
                    startsAt=starts_at,
                    endsAt=None,
                    fingerprint=alert.fingerprint,
                    duration=None
                )
                print("firing数据成功写入")
            elif alert.status == "resolved":
                s_alert = await models.Alert.get(id=id)
                if not s_alert:
                    print("告警已恢复,但是找不到相应ID")
                    return {"message": "告警已恢复,但是找不到相应ID"}
                s_alert.status = "resolved"
                
                ends_at = datetime.fromisoformat(alert.endsAt[:-1])
                s_alert.endsAt = ends_at
                duration = (ends_at - starts_at).seconds
                
                s_alert.duration = duration
                # 保存更新
                await s_alert.save()
                print("resolved数据成功更新")
            else:
                print("输入格式不正确")
            # 查询所有的 Alert 记录
        alerts = await models.Alert.all()

        # 遍历并详细打印每一条记录
        for alert in alerts:
            print(f"id: {alert.id}")
            print(f"Fingerprint: {alert.fingerprint}")
            print(f"Status: {alert.status}")
            print(f"Labels: {alert.labels}")
            print(f"Annotations: {alert.annotations}")
            print(f"StartsAt: {alert.startsAt}")
            print(f"EndsAt: {alert.endsAt}")
            print(f"Duration: {alert.duration}")
            print("-" * 50)  # 分隔符，增加可读性
    except Exception as e:
        print(f"An error occurred: {e}")

    return {"message": "Alert received successfully"}

@app.get("/alert/all",response_model=List[scheams.RecordAlert])
async def alertall():
    all = await models.Alert.all()
    for alert in all:
        alert.startsAt = alert.startsAt.isoformat() if isinstance(alert.startsAt, datetime) else alert.startsAt
        alert.endsAt = alert.endsAt.isoformat() if isinstance(alert.endsAt, datetime) else alert.endsAt
    return all
    