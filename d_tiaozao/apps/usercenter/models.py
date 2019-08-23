from django.db import models
from apps.accounts.models import User
from apps.goodsIssue.models import Goods
# Create your models here.
class UserLog(models.Model):
    """用户日志"""
    OPERATE = ((1,"购买"),(2,"加入购物车"))
    goods_name = models.ForeignKey(Goods, verbose_name="用户发布的商品名称")
    user = models.ForeignKey(User, verbose_name="用户")
    # goods_name = models.ForeignKey(Goods, verbose_name="用户发布的商品名称", null=True, blank=True)

    ptime = models.DateTimeField(verbose_name="商品上传时间", auto_now_add=True)
    operate = models.CharField(choices=OPERATE, max_length=10, verbose_name="操作", default=None)


    class Meta:
        verbose_name = "用户日志"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.goods_name.name}:{self.goods_name.price}{self.goods_name.status}"


