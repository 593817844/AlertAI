from pydantic import BaseModel, fields, model_validator
import settings
from utils import tools


class UserRegisterRequest(BaseModel):
    """注册接口的请求数据结构"""
    mobile: str = fields.Field(pattern='^1[3-9]\d{9}', description='手机号')
    username: str =fields.Field(description='用户名')
    password: str = fields.Field(min_length=6, max_length=16, description='密码')
    email: str


    @model_validator(mode='after')
    def model_validator(self):
        # 对密码进行哈希加密
        hashing = tools.Hashing()
        self.password = hashing.hash(self.password)

        return self

class LoginRequest(BaseModel):
    username: str
    password: str


