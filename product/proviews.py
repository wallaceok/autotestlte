from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#产品管理
# def product_manage(request):
#     username = request.session.get('user', '')
#     product_list = Product.objects.all()
#     return render(request, "product_manage.html", {"user": username, "products": product_list})

#产品管理
@login_required
def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    product_count = Product.objects.all().count()  # 统计产品数
    paginator = Paginator(product_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数,默认为第 1 页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        product_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        product_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中，则显示最后一页内容
    return render(request, "product_manage.html", {"user": username, "products": product_list,"productcounts":product_count})  #把值赋给 productcounts 变量

# 搜索功能
@login_required
def productsearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_productname = request.GET.get("productname", "")
    product_list = Product.objects.filter(productname__icontains = search_productname)
    return render(request, 'product_manage.html', {"user": username, "products": product_list})


