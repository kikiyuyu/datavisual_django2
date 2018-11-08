
from django.db import models

# Create your models here.mo
class ContentProvider(models.Model):
    '''
    内容提供商
    '''
    name = models.CharField(u'CP名称', max_length=20)
    email = models.CharField(u'登录邮箱', max_length=20)
    password = models.CharField(u'密码', max_length=20)


    def __str__(self):
        return self.name


def get_CP(email_t, password_t):
    '''
    获取cp
    :param email:账号
    :param password:密码
    :return: ContentProvider
    '''
    try:
        cp = ContentProvider.objects.get(email=email_t)
    except ContentProvider.DoesNotExist:
        return 1
    if cp:
        if cp.password == password_t:
            return cp
        else:
            return 3
    return 1

def register_CP(name_t, email_t, password_t):
    '''
    注册cp
    :param name_t:
    :param email_t:
    :param password_t:
    :return:boolen
    '''
    cp, status = ContentProvider.objects.get_or_create(email=email_t)
    if status:
        cp.password = password_t
        cp.name = name_t
        cp.save()

    return status