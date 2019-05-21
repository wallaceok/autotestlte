from django.shortcuts import render
from bug.models import Bug
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#bug管理
def bug_manage(request):
	username = request.session.get('user', '')
	bug_list = Bug.objects.all()
	bug_count = Bug.objects.all().count()
	paginator = Paginator(bug_list,8)  # 生成 paginator 对象，设置每页显示 8 条记录
	page = request.GET.get('page',1)		#获取当前的页码数，默认为第 1 页
	currentPage=int(page)	#把获取的当前页码数转换成整数类型
	try:
		bug_list = paginator.page(page)  # 获取当前页码数的记录列表
	except PageNotAnInteger:
		bug_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
	except EmptyPage:
		bug_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中， # 则显示最后一页的内容
	return render(request, "bug_manage.html", {"user": username,"bugs": bug_list,"bugcounts": bug_count})


# 搜索功能
@login_required
def bugsearch(request):
	username = request.session.get('user', '')  # 读取浏览器登录 Session
	search_bugname = request.GET.get("bugname", "")
	bug_list = Bug.objects.filter(bugname__icontains = search_bugname)
	return render(request, 'bug_manage.html', {"user": username, "bugs": bug_list})



