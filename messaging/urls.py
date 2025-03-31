from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='messaging_index'),
    path('list/', views.message_list, name='message_list'),
    path('<int:pk>/', views.message_detail, name='message_detail'),
    path('send/', views.send_message, name='send_message'),
]
