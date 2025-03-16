from django.urls import include, path
from .views import home_screen_view

urlpatterns = [
    path('', home_screen_view, name='landing'),
    path('accounts/', include('accounts.urls')),
]
