# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.db.models import Q

from .models import Blog, Label


def home(request):
    return HttpResponseRedirect(reverse('blog:index', args=('0', 'noKeyWords', 1)))


def index(request, *args, **kwargs):
    label_list = Label.objects.all()
    # 获得参数
    global blog_list
    label_id = kwargs.get('label_id')
    key_words = kwargs.get('key_words')
    page_id = int(kwargs.get('page_id'))

    # 根据条件查询博客
    if label_id != '0' and key_words != 'noKeyWords':
        blog_list = Blog.objects.filter(
            Q(status__name='发布', label=label_id, title__contains=key_words) |
            Q(status__name='发布', label=label_id, content__contains=key_words) |
            Q(status__name='发布', label=label_id, label__name__contains=key_words)).distinct().order_by('-modify_date')
    if label_id != '0' and key_words == 'noKeyWords':
        blog_list = Blog.objects.filter(Q(status__name='发布', label=label_id)).distinct().order_by('-modify_date')
    if label_id == '0' and key_words != 'noKeyWords':
        blog_list = Blog.objects.filter(
            Q(status__name='发布', title__contains=key_words) |
            Q(status__name='发布', content__contains=key_words) |
            Q(status__name='发布', label__name__contains=key_words)).distinct().order_by('-modify_date')
    if label_id == '0' and key_words == 'noKeyWords':
        blog_list = Blog.objects.filter(Q(status__name='发布')).distinct().order_by('-modify_date')

    # 创建分页对象
    paginator = Paginator(blog_list, 10)
    # 根据当前页码,确定返回的数据
    current_page = paginator.page(page_id)
    return render(request, 'blog/index.html', locals())


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
