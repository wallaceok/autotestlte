from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from webtest.models import Webcase,Webcasestep
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# Web用例管理
@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user', '')  # 读取浏览器登录Session
    webcase_count = Webcase.objects.all().count()
    paginator = Paginator(webcase_list,8)   #生成paginator对象，设置每页8条记录
    page = request.GET.get('page',1)  #获取当前页的页码数，默认为第一页
    currentPage = int(page)
    try:
        webcase_list = paginator.page(page)  #获取当前页码数据的记录列表
    except PageNotAnInteger:
        webcase_list = paginator.page(1)  #如果输入的页数不是整数，则显示第1页的内容
    except EmptyPage:
        webcase_list = paginator.page(paginator.num_pages) #如果输入的页数不在系统的页数中，则显示最后一页
    return render(request, "webcase_manage.html", {"user": username, "webcases": webcase_list,"webcasecounts":webcase_count})

# Web用例测试步骤
@login_required
def webcasestep_manage(request):
    username = request.session.get('user', '')
    webcasestep_list = Webcasestep.objects.all()
    webcaseid = request.GET.get('webcase.id', None)
    webcase = Webcase.objects.get(id=webcaseid)
    paginator = Paginator(webcasestep_list, 8)  # 生成paginator对象，设置每页8条记录
    page = request.GET.get('page', 1)  # 获取当前页的页码数，默认为第一页
    currentPage = int(page)
    try:
        webcasestep_list = paginator.page(page)  # 获取当前页码数据的记录列表
    except PageNotAnInteger:
        webcasestep_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第1页的内容
    except EmptyPage:
        webcasestep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页
    return render(request, "webcasestep_manage.html", {"user": username, "webcase": webcase,"webcasesteps": webcasestep_list})

# 搜索功能
@login_required
def websearch(request):
    username = request.session.get('user', '') # 读取浏览器登录 Session
    search_webcasename = request.GET.get("webcasename", "")
    webcase_list = Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request,'webcase_manage.html', {"user": username,"webcases":webcase_list})

# web步骤 搜索功能
@login_required
def webstepsearch(request):
    username = request.session.get('user', '') # 读取浏览器登录 Session
    search_webcasename = request.GET.get("webcasename", "")
    webcasestep_list = Webcasestep.objects.filter(webcasename__icontains=search_webcasename)
    return render(request,'webcasestep_manage.html', {"user":username,"webcasesteps":webcasestep_list})


