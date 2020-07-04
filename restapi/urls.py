from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.to_do, name='todo'),
    path('task-list/',views.tklist,name='todo-view'),
    path('task-detail/<str:pk>/',views.tkdetail,name='todo-detail'),
    path('task-create/',views.tkcreate,name='todo-create'),
    path('task-update/<str:pk>/',views.tkupdate,name='todo-detail'),
    path('task-delete/<str:pk>/',views.tkdelete,name='todo-delete'),
]

