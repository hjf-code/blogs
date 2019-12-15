import uuid

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# models.py是Web应用数据库的定义文件, 以Python类的形式定义数据库中的各个表.
# Create your models here.


# 状态: 草稿, 发布, 删除
class Status(models.Model):
    # 主键使用UUID, 这里的default使用的是uuid.uuid4而不是uuid.uuid4(),uuid.uuid4()为函数的返回值, 只调用一次,
    # 以后新建函数都用第一次返回的值, 而uuid.uuid4为函数, 每次新建对象都会调用一次函数
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 名称
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# 标签
class Label(models.Model):
    # 主键使用UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 名称
    name = models.CharField(max_length=30)
    # 博客数量
    count = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.name


# 博客
class Blog(models.Model):
    # 主键使用UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 标题
    title = models.CharField(max_length=50)
    # 内容
    content = RichTextUploadingField(null=True, blank=True)
    # 所属标签, 不直接级联删除, 若有子节点, 抛出ProtectedError异常
    label = models.ManyToManyField(Label)
    # 状态, 不直接级联删除, 若有子节点, 抛出ProtectedError异常
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    # 修改时间
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
