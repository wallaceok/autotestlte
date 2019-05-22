import pymysql
from apitest.models import Apitest,Apistep,Apis
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import HTMLTestRunner


def test(request):
	return HttpResponse("Here's the text of the Web page.")
# def login(request):
# 	return render(request,'login.html')

def login(request):
	if request.POST:
		username = password = ''
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			request.session['user'] = username
			response = HttpResponseRedirect('/home/')
			return response
		else:
			return render(request,'login.html', {'error': 'username or password error'})
	else:
		context = {}
		return render(request, 'login.html', context)
	return render(request, 'login.html')
def home(request):
	return render(request,"home.html")

def logout(request):
	auth.logout(request)
	return render(request,'login.html')

@login_required
def apis_manage(request):
	username = request.session.get('user', '')
	apis_list = Apis.objects.all()
	return render(request, "apis_manage.html", {"user": username, "apiss": apis_list})

# # 接口管理
# @login_required
# def apitest_manage(request):
# 	apitest_list = Apitest.objects.all() #读取所有流程接口数据
# 	username = request.session.get('user', '') # 读取浏览器登录Session
# 	return render(request,"apitest_manage.html",{"user": username,"apitests":apitest_list})#定义流程接口数据的变量并返回到前端

# 流程接口管理
@login_required
def apitest_manage(request):
	apitest_list = Apitest.objects.all()	#获取所有接口测试用例
	username = request.session.get('user', '') # 读取浏览器登录 Session
	apitest_count = Apitest.objects.all().count()
	paginator = Paginator(apitest_list, 8)	#生成 paginator 对象，设置每页显示 8 条记录
	page = request.GET.get('page',1)	#获取当前的页码数，默认为第 1 页
	currentPage=int(page)	#把获取的当前页码数转换成整数类型
	try:
		apitest_list = paginator.page(page)#获取当前页码数的记录列表
	except PageNotAnInteger:
		apitest_list = paginator.page(1)#如果输入的页数不是整数，则显示第 1 页内容
	except EmptyPage:
		apitest_list = paginator.page(paginator.num_pages)#如果输入的页数不在系统的页数# 中，则显示最后一页内容
	return render(request,"apitest_manage.html",{"user": username,"apitests":apitest_list,"apitestcounts":apitest_count})



# 接口步骤管理
# @login_required
# def apistep_manage(request):
# 	username = request.session.get('user', '')
# 	apistep_list = Apistep.objects.all()
# 	return render(request, "apistep_manage.html", {"user": username,"apisteps": apistep_list})
@login_required
def apistep_manage(request):
	username = request.session.get('user', '')
	apistep_list = Apistep.objects.all()
	apitestid = request.GET.get('apitest.id', None)
	apitest = Apitest.objects.get(id=apitestid)
	return render(request, "apistep_manage.html", {"user": username,"apitest": apitest,"apisteps": apistep_list})


# 单一接口管理
@login_required
def apis_manage(request):
	username = request.session.get('user', '')
	apis_list = Apis.objects.all()
	apis_count = Apis.objects.all().count()
	paginator = Paginator(apis_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
	page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
	currentPage = int(page)  # 把获取的当前页码数转换成整数类型
	try:
		apis_list = paginator.page(page)  # 获取当前页码数的记录列表
	except PageNotAnInteger:
		apis_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
	except EmptyPage:
		apis_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，# 则显示最后一页内容
	return render(request, "apis_manage.html", {"user": username, "apiss": apis_list,"apiscounts": apis_count})


def welcome(request):
	return render(request, "welcome.html")





# 测试报告
@login_required
def test_report(request):
	username = request.session.get('user', '')

	apis_list = Apis.objects.all()
	apis_count = Apis.objects.all().count()  # 统计接口数
	db = pymysql.connect(user='root', db='autotest', passwd='root', host='127.0.0.1')
	cursor = db.cursor()
	sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
	aa = cursor.execute(sql1)
	apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
	sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
	bb = cursor.execute(sql2)
	apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
	db.close()
	return render(request, "report.html",{"user": username, "apiss": apis_list, "apiscounts": apis_count, "apis_pass_counts": apis_pass_count,"apis_fail_counts": apis_fail_count})  # 把值赋给apiscounts变量

#返回左边主页面
def left(request):
	return render(request,"left.html")


#搜索功能

@login_required
def apisearch(request):
	username = request.session.get('user', '')  # 读取浏览器登录 session
	search_apitestname = request.GET.get("apitestname", "")
	apitest_list = Apitest.objects.filter(apitestname__contains = search_apitestname)
	return render(request, 'apitest_manage.html', {"user": username, "apitests": apitest_list})


#单一接口 搜索功能
@login_required
def apissearch(request):
	username = request.session.get('user', '')  # 读取浏览器登录 Session
	search_apiname = request.GET.get("apiname", "")
	apis_list = Apis.objects.filter(apiname__icontains = search_apiname)
	return render(request, 'apis_manage.html', {"user": username, "apiss": apis_list})

# 搜索功能
@login_required
def apistepsearch(request):
	username = request.session.get('user', '') # 读取浏览器登录 Session
	search_apiname = request.GET.get("apiname", "")
	apistep_list = Apistep.objects.filter(apiname__icontains=search_apiname)
	return render(request,'apistep_manage.html', {"user": username,"apisteps":apistep_list})








