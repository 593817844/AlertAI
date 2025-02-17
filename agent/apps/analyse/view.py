from fastapi import APIRouter
from openai import OpenAI
import os
from . import scheams


app=APIRouter()


async def read_prompt(path):
    with open(path,"r",encoding="utf-8") as file:
        prompt = file.read()
    return prompt
        

@app.post("/")
async def analyse(data: scheams.AgentRequest):
    # print(data.alerts)
    # print(data.system)
    
    alert_str=""
    for idx,alert in enumerate(data.alerts,1):
        alert_str += f"告警{idx}: {alert}"
    # print(alert_str)
    
    prompt = await read_prompt("prompts/prometheus.txt")
    
    output = prompt.replace("{{alerts}}", alert_str).replace("{{system-info}}", data.system)   
    print(output)
    
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"), 
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-max", # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'user', 'content': output}],
        )
        
    print(completion.to_dict()["choices"][0]["message"]["content"])
    return completion.to_dict()["choices"][0]["message"]["content"]