from django.contrib import admin
#电影模型添加到管理员
from .models import Movie
admin.site.register(Movie)

# Register your models here.
