# coding=utf-8
import logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
from django.conf import settings

logger = logging.getLogger('blog.views')


def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC}


# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponse('注册成功!!')
    else:
        uf = UserForm()
    return render(request, 'regist.html', {'uf': uf})


# 登陆
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/blog/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 60)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/blog/login/')
    else:
        uf = UserForm()
    return render(request, 'login.html', {'uf': uf})


# 登陆成功
def index(request):
    username = request.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})


# 退出
def logout(request):
    response = HttpResponse('退出成功!!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return response


#
def simple(request):
    try: myfile = open('etx.txt')
    except Exception, e:
        logger.error(e)
        #logger.debug(e)
    return render(request, 'simple.html')

