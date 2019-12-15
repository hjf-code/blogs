 #!/usr/bin/env python
# manage.py是系统自动生成的Django项目管理程序, Django项目创建和运行所需要的所有命令都能由这个脚本提供.
# 如为项目创建数据库的makemigrations和migrate, 启动服务器的runserver等. 编程过程中, manage.py一般是不需要修改的.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogs.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
