from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^index-(?P<label_id>\S+)-(?P<key_words>\S+)-(?P<page_id>\d+)', views.index, name='index'),
    path('detail/<slug:pk>', views.DetailView.as_view(), name='detail'),
]
