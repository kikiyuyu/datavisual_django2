from django.contrib import admin
import xadmin
from .models import *

class GameAdmin(object):
    list_display = ('id','game_name','contentprovider')

# Register your models here.
xadmin.site.register(Game, GameAdmin)