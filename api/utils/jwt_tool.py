import uuid
from jose import jwt
from datetime import timedelta, datetime
import settings
from typing import Optional


class JWTTool(object):
    """JWT工具类"""
    # 异常类
    JWTError = jwt.JWTError
    ExpiredSignatureError = jwt.ExpiredSignatureError

    def create_token(self, data: dict, expire_time: Optional[timedelta] = None):
        """
        生成JWT
        :param data: 需要进行JWT令牌加密的用户信息（解密的时候会用到）
        :param expire_time: 令牌有效期，单位：秒
        :return: jwt
        """
        now_time = datetime.utcnow()
        if expire_time:
            expire = now_time + timedelta(seconds=expire_time)
        else:
            expire = now_time + timedelta(seconds=settings.JWT['expire_time'])

        # 组装载荷数据的标准声明
        payload = {
            "exp": expire,  # 过期时间
            "iat": now_time,  # 生成时间
            "nbf": now_time,  # 启用时间
            "jti": str(uuid.uuid4())  # 唯一标记
        }
        # 组装载荷数据的公共声明
        payload.update(data)

        # 自动生成jwt
        return jwt.encode(payload, settings.JWT['secret_key'], algorithm=settings.JWT['algorithm'])

    def verify_token(self, token: str) -> dict:
        """
        验证token
        :param token: 客户端发送过来的token
        :return: 返回用户信息
        """
        payload = jwt.decode(token, settings.JWT['secret_key'], algorithms=settings.JWT['algorithm'])
        return payload


JwtToken = JWTTool()
