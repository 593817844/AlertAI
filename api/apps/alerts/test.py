import requests

# 设置要访问的 URL
url = "http://127.0.0.1:8000/alert/all"

# 发送 GET 请求
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    print("Request successful!")
    print("Response JSON:")
    print(response.json())  # 打印返回的 JSON 数据
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # 打印错误响应
