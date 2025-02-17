from fastapi import APIRouter,HTTPException
import httpx
from apps.alerts.models import Alert
from apps.systeminfo.models import SystemInfo
import json

app = APIRouter()


@app.post("/ai/{project}")
async def alertai(project: str):
    # 使用 filter 来筛选满足两个条件的记录
    alerts = await Alert.filter(
        status="firing",  # status 为 "firing"
        labels__contains={"project": project}  # labels 字段中包含 "instance": "server1"
    )
    # 获取系统信息
    systeminfo = await SystemInfo.filter(project=project).first()
    if not systeminfo:
        return "未找到对应的系统信息"
    if alerts:
        async with httpx.AsyncClient(timeout=httpx.Timeout(120)) as client:
            data={
                "alerts": [{"labels": alert.labels, "summary": alert.annotations["summary"], "id": alert.id} for alert in alerts] ,
                "system": systeminfo.architecture
            }
            print(data)
            response = await client.post("http://127.0.0.1:8080",json=data)
            if response.status_code == 200:
                result = response.json()  # 解析 JSON 响应
                print(result)  # 打印结果
                return result
            else:
                raise HTTPException(status_code=response.status_code, detail="Request failed")
    else:
        return "project中没找到firing相关的告警"
    return "Request failed"