from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import Goods
from apps.accounts.models import User
from .models import Goods
#用户商品发布
class PublishForm(forms.Form):
    # class Meta:
    #     model = Goods
    #     fields = ['name', 'price', 'ptime', 'context', 'img']

    name = forms.CharField(label="商品名称", required=True, error_messages={'required':'商品名不能为空'})
    price = forms.FloatField(label="商品价格",required=True)
    ptime = forms.DateField(required=True)
    # status = forms.ChoiceField(label="商品状态")
    context = forms.CharField(label="商品的描述", required=True, error_messages={'required':'商品名不能为空','max_length':'最多不超过100个字符'})
    # img = forms.ImageField(label="商品的图片", required=True)



















