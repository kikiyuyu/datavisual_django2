from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('oh! this is my fisrt page!')
    return render(request, 'login.html')