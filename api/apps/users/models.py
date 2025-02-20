from tortoise import models, fields


class User(models.Model):
    # 字段列表
    id = fields.IntField(pk=True, description='主键')
    username = fields.CharField(max_length=255, unique=True, description='账户名')
    password = fields.CharField(max_length=255, description='密码')
    mobile = fields.CharField(max_length=15, index=True, description='手机')
    email = fields.CharField(max_length=255,index=True, description='邮件')
    created_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")
    deleted_time = fields.DatetimeField(null=True, description="删除时间")

    # 元数据
    class Meta:
        table = "user_info"
        description = "用户信息"

    def __repr__(self):
        return f"User (id={self.id}, username={self.username})"

    __str__ = __repr__
