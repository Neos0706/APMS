from django.shortcuts import render

# Create your views here.
def news(request):
    # 获取当前请求的用户名
    username = request.user.username
    return render(request, 'news.html', locals())