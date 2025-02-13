import requests

# 设置数据
project = "ai"
architecture = '''
简介：该系统是AI告警辅助分析系统，技术选型vue、python、fastapi、mysql
架构：192.168.100.101是mysql服务器；192.168.100.102是前端web服务器；192.168.100.103是后端web服务器
部署方式：docker
'''

# 请求的URL
url = "http://127.0.0.1:8000/system/"

# 构建请求体
data = {
    "project": project,
    "architecture": architecture
}

# 发送POST请求
response = requests.post(url, json=data)

# 检查响应状态并输出结果
if response.status_code == 200:
    print("Data created successfully:")
    print(response.json())  # 打印返回的JSON响应
else:
    print(f"Failed to create data. Status code: {response.status_code}")
    print(response.text)
