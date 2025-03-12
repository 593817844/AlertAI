# 第一阶段：构建Vue应用
FROM node:14 AS build

# 设置工作目录
WORKDIR /app

# 将package.json和package-lock.json复制到容器中
# COPY package*.json ./

# 将整个项目复制到容器中
COPY ../../ui/ .

# 安装项目依赖
RUN npm install

# 运行npm run build命令进行打包
RUN npm run build


# 基础镜像
FROM nginx
# author
MAINTAINER timmy

# 挂载目录
VOLUME /home/twen/twen-ui
# 创建目录
RUN mkdir -p /home/twen/twen-ui
# 指定路径
WORKDIR /home/twen/twen-ui

# 复制html文件到路径
COPY --from=build /app/dist/ /home/twen/twen-ui

# 复制conf文件到路径
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
