from django.urls import path
from . import views

urlpatterns = [
    path('', views.digitalcontent_view, name='digitalcontent'),  # URL for the digitalcontent page
]