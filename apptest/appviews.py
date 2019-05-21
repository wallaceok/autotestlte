from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apptest.models import Appcase,Appcasestep

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# app用例管理
@login_required
def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    username = request.session.get('user', '')  # 读取浏览器登录Session
    paginator = Paginator(appcase_list,8)  # 生成 paginator 对象,设置每页显示 8 条记录
    page = request.GET.get('page',1)	#获取当前的页码数,默认为第 1 页
    currentPage=int(page)	#把获取的当前页码数转换成整数类型
    try:
        appcase_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        appcase_list = paginator.page(1)  # 如果输入的页数不是整数则显示第 1 页的内容
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中则显示最后一页的内容
    return render(request, "appcase_manage.html", {"user": username, "appcases": appcase_list})


# App用例测试步骤
@login_required
def appcasestep_manage(request):
    username = request.session.get('user','') #读取浏览器登录Session
    appcasestep_list = Appcasestep.objects.all()
    paginator = Paginator(appcasestep_list, 8)  # 生成 paginator 对象,设置每页显示 8 条记# 录
    page = request.GET.get('page', 1)  # 获取当前的页码数,默认为第 1 页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        appcasestep_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        appcasestep_list = paginator.page(1)  # 如果输入的页数不是整数则显示第 1 页的内容
    except EmptyPage:
        appcasestep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统# 的页数中则显示最后一页
    return render(request, "appcasestep_manage.html", {"user": username, "appcasesteps": appcasestep_list})


# App测试报告
@login_required
def apptest_report(request):
    username = request.session.get('user', '')
    return render(request, "apptest_report.html")

# 测试用例 搜索功能
@login_required
def appsearch(request):
    username = request.session.get('user', '') # 读取浏览器登录 Session
    search_appcasename = request.GET.get("appcasename", "")
    appcase_list = Appcase.objects.filter(appcasename__icontains=search_appcasename)

    return render(request,'appcase_manage.html', {"user": username,"appcases":appcase_list})

# 测试步骤搜索功能
@login_required
def appstepsearch(request):
    username = request.session.get('user', '') # 读取浏览器登录 Session
    search_appcasename = request.GET.get("appcasename", "")
    appcasestep_list = Appcasestep.objects.filter(appcasename__icontains=search_appcasename)
    return render(request,'appcasestep_manage.html', {"user":username,"appcasesteps":appcasestep_list})






