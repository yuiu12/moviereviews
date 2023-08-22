from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')
# Create your views here.
#自定义路径的内容设置
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
