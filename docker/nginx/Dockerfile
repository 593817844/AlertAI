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
# 复制conf文件到路径
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
# 复制html文件到路径
COPY ./dist /home/twen/twen-ui