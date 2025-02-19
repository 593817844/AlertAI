FROM python:3.10

# 设置工作目录
WORKDIR /agent

# 复制应用程序文件到工作目录
COPY ../../agent /agent

# 安装项目依赖框架
# 使用清华源安装依赖包
RUN pip install -U -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && pip list


ENV TIMEZONE=Asia/Shanghai

# 暴露应用程序监听的端口
EXPOSE 8000

# 启动Python应用程序，并使用 0.0.0.0:8000 监听所有可用地址
CMD ["python", "main.py"]
