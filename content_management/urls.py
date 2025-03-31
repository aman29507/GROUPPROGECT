from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='content_index'),
    path('list/', views.content_list, name='content_list'),
    path('<int:pk>/', views.content_detail, name='content_detail'),
    path('create/', views.content_create, name='content_create'),
]
