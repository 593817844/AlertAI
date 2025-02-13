from tortoise import models,fields

class SystemInfo(models.Model):
    id = fields.IntField(pk=True, description='唯一ID')
    project = fields.CharField(max_length=255,description='项目名称')
    architecture = fields.TextField(description='系统架构信息')
    
    class Meta:
        table = "systeminfo"
        description = "系统信息"
        
    def __repr__(self):
        return f"System info : (fingerprint={self.id}, status={self.project})"

    __str__ = __repr__