from django.shortcuts import render,HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import PublishForm
from apps.goodsIssue.models import Goods
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
def Issue(request):
    return HttpResponse("这是一个视图函数")
class Publish(View):
    # def get(self, request):
    #     form_2 = PublishForm()
    #     msg = '123'
    #     return render(request, "publish_goods.html", {"form_2":form_2, "msg":msg})
    def get(self, request):
        return render(request, 'publish_goods.html')
    def post(self, request):
        form = PublishForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            price = request.POST.get("price")
            status = request.POST.get("status")
            ptime = request.POST.get("ptime")
            context = request.POST.get("context")
            Goods.objects.create(name=name,price=price,status=status,ptime=ptime,context=context)



            # goods.price = request.POST.get("price")
            # request.goods_name.status = request.POST.get("status")
            # request.goods_name.ptime = request.POST.get("ptime")
            # request.goods_name.context = request.POST.get("context")
            # request.goods_name.save()
            return render(request, 'publish_goods.html')
        else:
            data = form.clean()
            error_msg = form.errors
            print(data)
            print(error_msg)
            return HttpResponse('Fail')

class Publish_new(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "publish_goods.html")

    def post(self, request):
        ret_info = {"code":200, "msg":"发布成功"}
        try:
            if request.POST.get("name"):
                request.goods_name.name = request.POST.get("name")
            if request.POST.get("price"):
                request.goods_name.price = request.POST.get("price")
            if request.POST.get("status"):
                request.goods_name.status = request.POST.get("status")
            if request.POST.get("ptime"):
                request.goods_name.ptime = request.POST.get("ptime")
            if request.POST.get("context"):
                request.goods_name.context = request.POST.get("context")
            # if request.POST.get("img"):
            #     request.goods_name.img = request.POST.get("img")
            request.goods_name.save()
        except Exception as ex:
            ret_info = {"code":200, "mag":"修改失败"}
        return render(request, "publish_goods.html", {"ret_info":ret_info})

def test(request):
    return render(request, "publish_goods.html")