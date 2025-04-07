from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_dashboard, name='member_dashboard'),  # Default dashboard route
    path('profile/', views.profile_view, name='profile'),
    # path('membership_status/', views.membership_status_view, name='membership_status'),
    # path('community_involvement/', views.community_involvement_view, name='community_involvement'),
    path('benefits/', views.benefits_view, name='benefits'),
    # path('events/', views.events_view, name='events'),
    # path('achievements/', views.achievements_view, name='achievements'),
]