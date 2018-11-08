from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # repassword = request.POST.get('repassword')
        # if password != repassword:
        #     return render(request, 'login.html', {'data': "两次的密码输入不相同"})
        cp = get_CP(email, password)
        if cp == 1:
            return render(request, 'login.html', {'data': '账号不存在'})
        elif cp == 3:
            return render(request, 'login.html', {'data': '密码错误'})
        else:
            return render(request, 'index.html', {'cp_name': cp.name})
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def register_perform(request):
    if request.method == 'POST':
        cpname = request.POST.get('cpname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password != repassword:
            return render(request, 'register.html', {'data': "两次的密码输入不相同"})
        if register_CP(cpname, email, password):
            return render(request, 'register.html', {'data': "账号注册成功"})
    return render(request, 'register.html', {'data': "账号已注册"})