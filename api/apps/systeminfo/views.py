from fastapi import APIRouter,HTTPException,Depends,Query,Request
from . import scheams, models
from utils import logs
from utils.jwt_tool import get_current_user
import os

logger = logs.getLogger(os.environ.get('APP_NAME'))

app = APIRouter()




@app.post("/system/",response_model=scheams.SystemResponse)
async def creat_systeminfo(s: scheams.SystemCreate,current_user: dict = Depends(get_current_user)):
    system = await models.SystemInfo.create(**s.dict())
    return scheams.SystemResponse(id=system.id,project=system.project,architecture=system.architecture)

@app.put("/system/{system_id}", response_model=scheams.SystemResponse)
async def update_systeminfo(system_id: int, s: scheams.SystemCreate,current_user: dict = Depends(get_current_user)):
    # 尝试获取要更新的系统信息
    system = await models.SystemInfo.get_or_none(id=system_id)
    
    if system is None:
        raise HTTPException(status_code=404, detail="System not found")
    
    # 更新系统信息
    await system.update_from_dict(s.dict())
    await system.save()
    
    return scheams.SystemResponse(id=system.id, project=system.project, architecture=system.architecture)

@app.delete("/system/{system_id}", response_model=dict)
async def delete_systeminfo(system_id: int,current_user: dict = Depends(get_current_user)):
    # 尝试获取要删除的系统信息
    system = await models.SystemInfo.get_or_none(id=system_id)
    
    if system is None:
        raise HTTPException(status_code=404, detail="System not found")
    
    # 删除系统信息
    await system.delete()
    
    return {"detail": "System deleted"}

@app.get('/system')
async def get_systeminfo(request: Request, page: int = Query(1, alias='page', ge=1), size: int = Query(10, alias='size', ge=1, le=100),current_user: dict = Depends(get_current_user)):
    """查询所有用户，并支持分页"""
    # 计算分页的偏移量
    offset = (page - 1) * size
    
    # 获取分页数据
    users = await models.SystemInfo.all().offset(offset).limit(size)

    # 获取总记录数
    total_users = await models.SystemInfo.all().count()

    # 返回分页数据和总记录数
    return {
        "code": 200,
        "status": "Success",
        "err_msg": "查询成功",
        "data": users,
        "total": total_users,
        "page": page,
        "size": size
    }