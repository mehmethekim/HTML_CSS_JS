from django.urls import path
from . import views
urlpatterns = [
    path("", views.index , name = "index"),
    path("mehmet",views.mehmet, name = "mehmet page"),
    path("<str:name>",views.input , name  = "input page ")
]