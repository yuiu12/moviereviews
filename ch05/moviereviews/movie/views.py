from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # return HttpResponse('<h1>Welcome to Home Page</h1>')
    searchTerm = request.GET.get('searchMovie')
    # return render(request,'home.html',{'name':'GregLim'})
    return render(request, 'home.html', {'searchTerm':searchTerm})

# Create your views here.
#自定义路径的内容设置
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
def signup(request):
    email = request.GET.get('email')
    return  render(request,'signup.html',{'email':email})