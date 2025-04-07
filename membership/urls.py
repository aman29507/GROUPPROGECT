from django.urls import path
from . import views
from users.views import users_view

urlpatterns = [
    path('', views.membership_view, name='membership'),  # URL pattern for the "Users" page

    path('select/', views.membership_select, name='membership_select'),  # New URL for membership selection
    path('save-interests/', views.save_interests, name='save_interests'),
    path('users/',users_view,name = 'users'),
]

