from django.contrib import admin
import xadmin
from .models import *

class RegisterAdmin(object):
    list_display = ('id', 'game_id', 'total_register', 'total_male', 'total_female',)

# Register your models here.
xadmin.site.register(Register, RegisterAdmin)