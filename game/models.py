from django.db import models

# Create your models here.
class Game(models.Model):
    '''
    游戏
    '''
    game_name = models.CharField(u'游戏名字', max_length=20)