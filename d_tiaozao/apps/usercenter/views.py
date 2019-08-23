from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Goods, UserLog
from apps.accounts.models import User
# Create your views here.
def test(request):
    return HttpResponse("个人中心视图")

def Message(request):
    return render(request, 'error_msg.html')

# @login_required
# def Goods_list(request):
#     g_list = Goods.objects.all()[:10]
#     status = dict(Goods.STATUS)
#     for g in g_list:
#         g.status_cn = status[int(g.status)]
#     recent_user_ids = [item['user'] for item in Goods.objects.filter(status=1).values('user').distinct()[:10]]
#     recent_user = User.objects.filter(id__in=recent_user_ids)
#     kwgs = {
#         "g_list":g_list,
#         "recent_user":recent_user
#     }
#     return render(request, "index.html", kwgs)

#商品发布模块
# @login_required
def index(request):
    userlog = UserLog.objects.all()
    # operator = dict(UserLog.OPERATE)
    # for log in userlog:
    #     log.operate_cn = operator[int(log.operate)]
    recent_user_ids = [item['user'] for item in UserLog.objects.values('user')]
    recent_user = User.objects.filter(id__in=recent_user_ids)
    kwgs = {
        "userlog":userlog,
        "recent_user":recent_user
    }
    return render(request, 'base.html', kwgs)

@login_required
def Index(request):
    userlog = UserLog.objects.all()
    # operator = dict(UserLog.OPERATE)
    # for log in userlog:
    #     log.operate_cn = operator[int(log.operate)]
    recent_user_ids = [item['user'] for item in UserLog.objects.values('user')]
    recent_user = User.objects.filter(id__in=recent_user_ids)
    kwgs = {
        "userlog":userlog,
        "recent_user":recent_user
    }
    return render(request, 'index.html', kwgs)




