from django.db import models
from django.contrib.auth.models import AbstractUser
from easy_thumbnails.fields import ThumbnailerImageField
# Create your models here.
#继承自AbstractUser
class User(AbstractUser):
    #CharField => max_length
    #ImageField => Pillow 库
    realname = models.CharField(max_length=8, verbose_name="真实姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    qq = models.CharField(max_length=11, verbose_name="QQ号")
    avator_sor = ThumbnailerImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")