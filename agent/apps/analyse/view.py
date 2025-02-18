from fastapi import APIRouter
from openai import OpenAI
import os
from . import scheams
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

app=APIRouter()


async def read_prompt(path):
    with open(path,"r",encoding="utf-8") as file:
        prompt = file.read()
    return prompt

async def alerts_messages(alerts):
    alert_str=""
    for idx,alert in enumerate(alerts,1):
        alert_str += f"告警{idx}: {alert}"
    return alert_str

# @app.post("/")
# async def analyse(data: scheams.AgentRequest):
#     # print(data.alerts)
#     # print(data.system)
    
#     alert_str=""
#     for idx,alert in enumerate(data.alerts,1):
#         alert_str += f"告警{idx}: {alert}"
#     # print(alert_str)
    
#     prompt = await read_prompt("prompts/prometheus.txt")
    
#     output = prompt.replace("{alerts}", alert_str).replace("{system_info}", data.system)   
#     print(output)
    
#     client = OpenAI(
#         # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
#         api_key=os.getenv("DASHSCOPE_API_KEY"), 
#         base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     )
#     completion = client.chat.completions.create(
#         model="qwen-max", # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
#         messages=[
#             {'role': 'user', 'content': output}],
#         )
        
#     print(completion.to_dict()["choices"][0]["message"]["content"])
#     return completion.to_dict()["choices"][0]["message"]["content"]


@app.post("/")
async def qianwen(data: scheams.AgentRequest):
    # 设置 API Key 和 base_url
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    # 创建 ChatOpenAI 实例
    chat = ChatOpenAI(
        model="qwen-max",  # 使用 qwen-plus 模型
        openai_api_base=base_url,  # 设置 base_url
    )
    template = await read_prompt("prompts/prometheus.txt")

    prompt = PromptTemplate(input_variables=["alerts","system_info"], template=template)
    
    alerts = await alerts_messages(data.alerts)
    system_info = data.system

    # 填充模板
    input_prompt = prompt.format(alerts=alerts,system_info=system_info)
    # print(input_prompt)

    # 定义系统消息和用户消息
    messages = [
        # SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=input_prompt),  # 使用填充后的提示词
    ]

    # 调用模型
    response = await chat.ainvoke(messages)
    # 打印响应
    print(response.content)
    return response.content
