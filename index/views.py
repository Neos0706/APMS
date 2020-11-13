from django.http import HttpResponse
from django.shortcuts import render
from user.models import MyUser

# Create your views here.


def index(request):
    # 获取当前请求的用户名
    username = request.user.username
    return render(request, 'index.html', locals())




