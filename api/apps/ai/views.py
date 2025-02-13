from FastAPI import APIRouter,HTTPException
import httpx
from apps.alerts.models import Alert
from apps.systeminfo.models import SystemInfo
app = APIRouter()


@app.post("/ai/{project}")
async def alertai(project: str):
    # 使用 filter 来筛选满足两个条件的记录
    alerts = await Alert.filter(
        status="firing",  # status 为 "firing"
        labels__project=project  # labels 字段中包含 "instance": "server1"
    )
    system = SystemInfo.get(project=project)
    if alert:
        async with httpx.AsyncClient() as client:
            data={
                "alert": alerts.values(),
                "system": system
            }
            response = await client.post("http://127.0.0.1/agent",json=data)
            if response.status_code == 200:
                result = response.json()  # 解析 JSON 响应
                print(result)  # 打印结果
                return result
            else:
                raise HTTPException(status_code=response.status_code, detail="Request failed")
    else:
        return "project中没找到firing相关的告警"
    return {"status":"success",result:"......"}