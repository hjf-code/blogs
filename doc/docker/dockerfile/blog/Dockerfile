FROM tnir/mysqlclient:1.4.2

MAINTAINER paulandcode

# 定义需要的版本
ENV DJANGO_VER 2.0
ENV CKEDITOR_VER 5.8.0

# 安装django和ckeditor
RUN pip install django==$DJANGO_VER -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip install django-ckeditor==$CKEDITOR_VER -i https://mirrors.aliyun.com/pypi/simple/

# 暴露的端口
EXPOSE 8080

# 定义匿名卷
VOLUME /project

# 运行服务的命令
CMD ["python3", "/project/blogs/manage.py", "runserver", "0.0.0.0:8080"]
