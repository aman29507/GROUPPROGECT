from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='events_index'),
    path('list/', views.event_list, name='event_list'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.event_create, name='event_create'),
]
