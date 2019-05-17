from django.contrib import admin
from product.models import Product
from apitest.models import Apitest,Apis
from apptest.models import Appcase

from webtest.models import Webcase

class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']
    model = Apis
    extra = 1

class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename', 'apptestresult', 'create_time', 'id','product']
    model = Appcase
    extra = 1

class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult', 'create_time', 'id', 'product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    inlines = [WebcaseAdmin]
admin.site.register(Product,ProductAdmin) # 把产品模块注册到Django admin后台并能显示



