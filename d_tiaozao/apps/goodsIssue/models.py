from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.accounts.models import User
from d_tiaozao.settings import MEDIA_ROOT, THUMB_SIZE
from apps.accounts.libs_images import make_thumb
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.fields.files import ImageFieldFile
import os
class Goods(models.Model):
    #  商品详情
    STATUS = (
        (1, "在售"),
        (2, "缺货"),
        (3, "下架"),
    )
    name = models.CharField(verbose_name='商品名称', max_length=255, default=None)
    price = models.FloatField(verbose_name="商品价格", default=None)
    # discount = models.FloatField(verbose_name="商品折扣", default=None)
    status = models.IntegerField(verbose_name="商品状态", choices=STATUS, default=None)
    ptime = models.DateTimeField("上架时间", auto_now=True)
    context = models.TextField(verbose_name="商品描述", help_text="这是商品简介，请不要超过100个字", default=None)
    img = models.ImageField(verbose_name="商品图片", upload_to='goods/%Y%m%d', default='goods/beauty_1.jpg')
    owner = models.ForeignKey(User, verbose_name="商品拥有者", null=True)
    def save(self, *args, **kwargs):
        #将上传的图片保存
        super().save()
        #如果是默认图片不压缩
        if self.img.name == 'goods/beauty_1.jpg':
            return
        #如果文件不存在，不压缩
        if not os.path.exists(os.path.join(MEDIA_ROOT, self.img.name)):
            return
        base, ext = os.path.splitext(self.img.name)
        #从头像中生成缩略图
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.img.name), size=THUMB_SIZE)

        # if thumb_pixbuf:
        #     #缩略图的保存文件全路径 = > 保存文件
        #     thumb_path = os.path.join(MEDIA_ROOT, base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext)


    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name
        #定义权限 => auth_permission表插入数据
        permissions = (
            ('can_change_goods_status', "可以修改商品状态"),
            ('can_add_goods', "可以添加商品")
        )

    def __str__(self):
        return f"{self.id}:{self.img}"

