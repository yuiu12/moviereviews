from django.urls import path 
from . import views
#整数的电影的主键 我们数据库模型添加了一个自动递增的主键 
urlpatterns = [
    path('<int:movie_id>',views.detail,name='detail')

]