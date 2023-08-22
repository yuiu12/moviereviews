from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
def home(request):
    # return HttpResponse('<h1>Welcome to Home Page</h1>')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    # return render(request,'home.html',{'name':'GregLim'})
    #传递到home.html里面
    return render(request, 'home.html', {'searchTerm':searchTerm,'movies':movies})

# Create your views here.
#自定义路径的内容设置
def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
def signup(request):
    email = request.GET.get('email')
    return  render(request,'signup.html',{'email':email})