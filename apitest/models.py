from django.db import models
from product.models import Product

class Apitest(models.Model):
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    #关联产品ID，其中product是应用名，Product是product应用的表名
    apitestname = models.CharField('流程接口名称',max_length=64)
    apitestdesc = models.CharField('描述', max_length=64, null=True)  # 流程接口描述
    apitester = models.CharField('测试负责人', max_length=16)  # 执行人
    apitestresult = models.BooleanField('测试结果')  # 流程接口测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取# 当前时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'
    def __str__(self):
        return self.apitestname
class Apistep(models.Model):
    Apitest = models.ForeignKey(Apitest,on_delete=models.CASCADE,)  # 关联接口ID
    apiname = models.CharField('接口名称', max_length=100)  # 接口标题
    apiurl = models.CharField('url地址', max_length=200)  # 地址
    apistep = models.CharField('测试步聚', max_length=100, null=True)  # 测试步聚
    apiparamvalue = models.CharField('请求参数和值', max_length=800)  # 参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200,null=True)  # 请求方法
    apiresult = models.CharField('预期结果', max_length=200)  # 预期结果
    apistep = models.CharField('测试步聚', max_length=100, null=True)  # 测试步聚
    apistatus = models.BooleanField('是否通过')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获# 取当前时间

    def __str__(self):
        return self.apiname

class Apis(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品ID
    producter = models.CharField('产品负责人', max_length = 200, null = True)  # 产品负责人
    apiname = models.CharField('接口名称', max_length=100)  # 接口标题
    apiurl = models.CharField('url地址', max_length=200)  # 地址
    apiparamvalue = models.CharField('请求参数和值', max_length=800)  # 请求参数和值
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='0', max_length=200)  # 请求方法
    apiresult = models.CharField('预期结果', max_length=200)  # 预期结果
    apistatus = models.BooleanField('是否通过')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取# 当前时间
    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'

    def __str__(self):
        return self.apiname