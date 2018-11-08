from django.db import models
from contentprovider.models import *
# Create your models here.
class Game(models.Model):
    '''
    游戏
    '''
    game_name = models.CharField(u'游戏名字', max_length=20)
    contentprovider = models.ForeignKey(ContentProvider, u'cp名称',related_name="primary_storys")

    def __str__(self):
        return "%s-%s" % (self.game_name, self.contentprovider.name)