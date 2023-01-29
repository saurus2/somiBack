from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.getTestDatas, name="test01datas"),
]