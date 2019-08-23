from django.shortcuts import render,HttpResponse

# Create your views here.
# def base(request):
#     return render(request,"base.html")

def index(request):
    return render(request, "index.html")

def goods_list(request):
    return render(request, "goods_list.html")

def buy_hostory(request):
    return render(request, 'buy_history.html')

def goods_detail(request):
    return render(request, 'goods_detail.html')

def sale_history(request):
    return render(request, 'sale_history.html')

def user_issue(request):
    return render(request, "user_issue.html")

def user_register(request):
    return render(request, "user_register.html")

