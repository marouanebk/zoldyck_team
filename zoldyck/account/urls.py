from django.urls import include, re_path,path
from . import views


app_name = 'account'
urlpatterns = [
    path("", views.home , name="home")

]
