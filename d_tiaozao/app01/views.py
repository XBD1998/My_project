from django.shortcuts import render,HttpResponse

# Create your views here.
def base(request):
    return render(request,"app01/base.html")

def index(request):
    return render(request, "app01/index.html")

def goods_list(request):
    return render(request, "app01/goods_list.html")

def buy_hostory(request):
    return render(request, 'app01/buy_history.html')

def goods_detail(request):
    return render(request, 'app01/goods_detail.html')

def sale_history(request):
    return render(request, 'app01/sale_history.html')

def user_issue(request):
    return render(request, "app01/user_issue.html")

def user_register(request):
    return render(request, "app01/user_register.html")

def login(request):
    return render(request, "app01/login.html")