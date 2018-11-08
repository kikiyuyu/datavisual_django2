from django.contrib import admin
import xadmin
from .models import *

class ContentProviderAdmin(object):
    list_display = ('id', 'name', 'email', 'password')

# Register your models here.
xadmin.site.register(ContentProvider, ContentProviderAdmin)