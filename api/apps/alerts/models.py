from tortoise import models, fields

class Alert(models.Model):
    # 字段列表
    id = fields.CharField(pk=True, max_length=255, description='唯一ID')
    fingerprint = fields.CharField(max_length=255, description='告警指纹')
    status = fields.CharField(max_length=50, description='告警状态')
    labels = fields.JSONField(description='标签存储，如 alertname, instance 等')
    annotations = fields.JSONField(description='注解存储，如 summary 等')
    startsAt = fields.DatetimeField(description='告警开始时间')
    endsAt = fields.DatetimeField(null=True, description='告警结束时间')
    duration = fields.IntField(null=True, description='持续时间') 

    # 元数据
    class Meta:
        table = "alerts"
        description = "告警信息"

    def __repr__(self):
        return f"Alert (fingerprint={self.id}, status={self.status})"

    __str__ = __repr__




