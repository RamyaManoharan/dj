from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("add",views.add,name="add"),
    path("register/",views.register,name="register")

]