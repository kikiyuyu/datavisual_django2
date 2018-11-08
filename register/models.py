from django.db import models

# Create your models here.
class Register(models.Model):
    '''
    注册人数
    '''
    game_id = models.IntegerField(u'游戏id')
    total_register = models.IntegerField(u'注册人数', default=0)
    create_time =  models.DateTimeField(u'创建时间')
    total_male = models.IntegerField(u'男性注册人数', default=0)
    total_female = models.IntegerField(u'女性注册人数', default=0)



def player_register(datetime, sex):
    '''
    新玩家注册
    :param datetime: 已日期作为key检索数据表
    :return: boolean
    '''
    if datetime:
        d = Register.objects.get(game_id=datetime)
        if d:
            d.total_register = d.total_register + 1
            if sex == 1:
                d.total_male = d.total_male + 1
            else:
                d.total_female = d.total_female + 1
            d.save()
        else:
            Register.objects.create()

        d =  Register.objects.filter(game_id__exact=datetime)
    else:
        return False

def get_register_list(start_date, end_date):
    '''
    查询注册信息
    :param start_date: 查询开始时间
    :param end_date: 查询结束时间
    :return: list
    '''
