CREATE TABLE alerts (
    id VARCHAR(255) PRIMARY KEY,
    fingerprint VARCHAR(255) NOT NULL,  -- 主键字段
    status VARCHAR(50) NOT NULL,            -- 告警状态字段
    labels JSON NOT NULL,                   -- 标签字段，存储 JSON 格式数据
    annotations JSON NOT NULL,              -- 注解字段，存储 JSON 格式数据
    startsAt DATETIME NOT NULL,             -- 告警开始时间字段
    endsAt DATETIME,                        -- 告警结束时间字段，可以为空
    duration INT                           -- 持续时间字段，可以为空
);
CREATE TABLE systeminfo (
    id SERIAL PRIMARY KEY,  -- 使用 SERIAL 自动生成唯一 ID
    project VARCHAR(255) NOT NULL,  -- 项目名称，最大长度为 255
    architecture TEXT  -- 系统架构信息
);