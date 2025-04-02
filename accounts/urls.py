from django.urls import path
from .views import signup_view, login_view, logout_view
from .views import admin_dashboard, approve_request, reject_request
from landing.views import home_screen_view
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve/<int:request_id>/', approve_request, name='approve_request'),
    path('reject/<int:request_id>/', reject_request, name='reject_request'),
    # path('',home_screen_view,name = 'home'),
]

