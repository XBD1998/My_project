from django.contrib import admin
from . models import User
from apps.goodsIssue.models import Goods
# Register your models here.
admin.site.register(User)
admin.site.register(Goods)
