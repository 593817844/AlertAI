from pydantic import BaseModel
from typing import List,Dict,Any

# class AgentRequest(BaseModel):
#     alerts: str
#     system: str
    
# 定义 alert 标签模型
class AlertLabels(BaseModel):
    ip: str
    app: str
    project: str
    instance: str
    severity: str
    alertname: str

# 定义 alert 模型
class Alert(BaseModel):
    labels: AlertLabels
    summary: str
    id: str

# 定义系统信息模型
class AgentRequest(BaseModel):
    # alerts: List[Alert]
    alerts: List[Dict[str, Any]]  # 可以接收未知结构的 alert 对象
    system: str
