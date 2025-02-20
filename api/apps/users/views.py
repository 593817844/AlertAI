from fastapi import APIRouter, HTTPException, status, Request,Query
from . import scheams, models
from utils.jwt_tool import JwtToken


app = APIRouter()


@app.post('/register')
async def register(request: Request, user_info: scheams.UserRegisterRequest):
    """处理用户注册请求"""
    # 1. 验证用户账号是否重复注册[mobile]
    user = await models.User.filter(mobile=user_info.mobile).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='当前手机已注册，不能重复注册！')

    # 3. 添加用户数据
    user = await models.User.create(
        username=user_info.mobile,
        password=user_info.password,
        mobile=user_info.mobile,
        email=user_info.email
    )

    # 4. 返回结构
    return {
        'id': user.id,
        'username': user.username,
        'mobile': user.mobile,
        'email': user.email,
        'code': status.HTTP_200_OK,
        'err_msg': '用户注册成功',
        'status': 'Success',
        'token': JwtToken.create_token({
            'id': user.id
        }),
    }


@app.delete('/user/{user_id}')
async def delete_user(request: Request, user_id: int):
    """处理用户删除请求（硬删除）"""
    # 1. 验证用户是否存在
    user = await models.User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")

    # 2. 执行硬删除
    await user.delete()

    # 3. 返回响应
    return {
        "code": status.HTTP_200_OK,
        "err_msg": "用户删除成功",
        "status": "Success"
    }

@app.get('/users')
async def get_users(request: Request, page: int = Query(1, alias='page', ge=1), size: int = Query(10, alias='size', ge=1, le=100)):
    """查询所有用户，并支持分页"""
    # 计算分页的偏移量
    offset = (page - 1) * size
    
    # 获取分页数据
    users = await models.User.all().offset(offset).limit(size)

    # 获取总记录数
    total_users = await models.User.all().count()

    # 返回分页数据和总记录数
    return {
        "code": status.HTTP_200_OK,
        "status": "Success",
        "err_msg": "查询成功",
        "data": users,
        "total": total_users,
        "page": page,
        "size": size
    }

@app.patch('/update_user/{user_id}')
async def update_user(request: Request, user_id: int, user_info: scheams.UserRegisterRequest):
    """更新用户信息"""
    # 1. 验证用户是否存在
    user = await models.User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")

    # 2. 更新用户字段
    if user_info.username:
        user.username = user_info.username
    if user_info.password:
        user.password = user_info.username
    if user_info.mobile:
        user.mobile = user_info.mobile
    if user_info.email:
        user.email = user_info.email
        

    # 3. 保存更新的数据
    await user.save()

    # 4. 返回响应
    return {
        "code": status.HTTP_200_OK,
        "err_msg": "用户信息更新成功",
        "status": "Success",
        "data": {
            "id": user.id,
            "username": user.username,
            "mobile": user.mobile,
            "email": user.email
        }
    }



@app.get('/login')
async def login():

    return {'methods': 'login'}