from django.shortcuts import render, redirect
from user.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from .models import MyUser as User
from .form import MyUserCreationForm
from django.contrib.auth import login, logout, authenticate
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from ap.models import *


# Create your views here.


def loginView(request):
    # 设置标题和另外两个URL链接
    title = '登录'
    unit_2 = '/user/register.html'
    unit_2_name = '立即注册'
    unit_1 = '/user/setpassword.html'
    unit_1_name = '修改密码'
    button = '马上登录'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    # 根据用户名查询对象
                    users = MyUser.objects.filter(username=username)  # 查询结果为一个列表
                    request.session['user_id'] = users[0].id  # 把用户id和名字放入session中
                    request.session['user_name'] = username
                return redirect('/')
            else:
                tips = '账号密码错误,请重新输入'
        else:
                tips = '用户不存在,请注册'
    return render(request, 'user.html', locals())


def registerView(request):
    if request.method == 'POST':
        user = MyUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            tips = '注册成功'
            user = MyUserCreationForm()
        else:
            tips ='注册失败'
    else:
        user = MyUserCreationForm()
    return render(request, 'register.html', locals())


def setpasswordView(request):
    title = '修改密码'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/register.html'
    unit_1_name = '立即注册'
    button = '确定修改密码'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            user.set_password(new_password)
            user.save()
            tips = '密码修改成功'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())


# 用户注销,退出登录
def logoutView(request):
    logout(request)
    return redirect('/')


# 找回密码
def findPassword(request):
    button = '获取验证码'
    new_password = False
    if request.method == 'POST':
        username = request.POST.get('username', 'root')
        VerificationCode = request.POST.get('VerificationCode', '')
        password = request.POST.get('password', '')
        user = User.objects.filter(username=username)
        # 用户不存在
        if not user:
            tips = '用户' + username + '不存在'
        else:
            # 判断验证码是否已发送
            if not request.session.get('VerificationCode', ''):
                # 发送验证码并将验证码写入session
                button = '重置密码'
                tips = '验证码已发送'
                new_password = True
                VerificationCode = str(random.randint(1000, 9999))
                request.session['VerificationCode'] = VerificationCode
                user[0].email_user('找回密码', VerificationCode)
            # 匹配输入的验证码是否正确
            elif VerificationCode == request.session.get('VerificationCode'):
                # 密码加密处理并保存到数据库
                dj_ps = make_password(password, None, 'pbkdf2_sha256')
                user[0].password = dj_ps
                user[0].save()
                del request.session['VerificationCode']
                tips = '密码已重置'
            # 输入验证码错误
            else:
                tips = '验证码错误,请重新获取'
                new_password = False
                del request.session['VerificationCode']
    return render(request, 'findPassword.html', locals())


@login_required(login_url='/user/login.html')
def user_center_infoView(request):
    user_email = MyUser.objects.get(id=request.session['user_id']).email

    # goods_ids = request.COOKIES.get('goods_ids', '')    #为str型
    # goods_ids1 = goods_ids.split(',')   #进行切片,获得list型
    goods_ids1 = request.session.get(str(request.session['user_id']), '')
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(Product.objects.get(id=int(goods_id)))
    context = {
               'user_name': request.session['user_name'],
               'user_email': user_email,
               'goods_list': goods_list,
               }
    return render(request, 'user_center_info.html', context)


@login_required(login_url='/user/login.html')
def user_center_orderView(request):
    return render(request, 'user_center_order.html', locals())


@login_required(login_url='/user/login.html')
def user_center_siteView(request):
    return render(request, 'user_center_site.html', locals())


