# 基于Docker与Django的个人博客

### 本人线上项目地址

https://www.paulandcode.com

### 项目部署

1. 部署方案: python3 + nginx + mysql + docker
    > 小项目没有用uwsgi 

2. 部署时删除项目中不相关文件
    + (1) /blogs/doc文件夹
    + (2) /blogs/.gitignore文件
    + (3) /blogs/LICENSE文件
    + (4) /blogs/README.md文件
    > 若不想使用日志, 可以删除/blogs/blogs/settings.py文件中logging相关配置, 并删除logs文件夹
    
3. 表结构及数据
    + (1) /blogs/doc/blog.sql文件中包含了所有表结构以及实际的170多个博客
    + (2) 项目前台地址为: 127.0.0.1
    + (3) 项目后台管理地址为: 127.0.0.1/a, 默认账号为admin, 密码为abc123456, 使用时请及时修改账号密码
    
4. 部署步骤
    + (1) 修改/blogs/doc/docker/compose/mysql/docker-compose.yml中的mysql密码(MYSQL_ROOT_PASSWORD属性), 并启动mysql容器. 
    + (2) 使用/blogs/doc/blog.sql文件导入表结构和数据, 并修改/blogs/blogs/settings.py文件中数据库ip和账号密码. 
    + (3) 使用/blogs/doc/docker/dockerfile/blog/Dockerfile文件构建blog:v1镜像.
    + (4) 使用/blogs/doc/docker/compose/blog/docker-compose.yml文件启动blog容器.
    + (5) 将整个项目(删除项目中不相关文件)复制到blog_project数据卷中, 重启blog容器.
    + (6) 使用/blogs/doc/docker/compose/nginx/docker-compose.yml文件启动nginx容器. 
    + (7) 参考/blogs/doc/docker/compose/nginx/default.conf, 修改nginx_config数据卷中的配置, 并重启nginx容器. 
    > 若想用https, 可以调整nginx配置, 请参考: https://help.aliyun.com/document_detail/98728.html
