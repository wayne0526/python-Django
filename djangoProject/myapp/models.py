from django.db import models


# Create your models here.
# 建立資料庫註冊欄位名
class register_account(models.Model):
    username_list = models.CharField(null=True, max_length=50, blank=True)
    password_list = models.CharField(max_length=50, null=True, blank=True)
    email_list = models.EmailField(max_length=50, null=True, blank=True)
    name_list = models.CharField(max_length=50, null=True, blank=True)
    phone_list = models.IntegerField(max_length=50, null=True, blank=True)
    gender_list = models.CharField(max_length=50, null=True, blank=True)
    birthday_list = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "dreamreal"


class Web(models.Model):
    url = models.CharField(null=True, max_length=500, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)
    title = models.EmailField(max_length=500, null=True, blank=True)
    money = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = "Web"
