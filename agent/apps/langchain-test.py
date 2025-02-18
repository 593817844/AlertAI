import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

# 设置 API Key 和 base_url
os.environ["OPENAI_API_KEY"] = "xxxxx"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 创建 ChatOpenAI 实例
chat = ChatOpenAI(
    model="qwen-max",  # 使用 qwen-plus 模型
    openai_api_base=base_url,  # 设置 base_url
)


# 创建一个提示词模板
template = "背诵一首{assistant_name}的诗"
prompt = PromptTemplate(input_variables=["assistant_name"], template=template)

# 填充模板
input_prompt = prompt.format(assistant_name="李白")

# 定义系统消息和用户消息
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=input_prompt),  # 使用填充后的提示词
]

# 调用模型
response = chat.invoke(messages)


# 打印响应
print(response.content)