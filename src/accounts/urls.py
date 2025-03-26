from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard_view, activity_report, include

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),  
    path('report/', activity_report, name='activity-report'),
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),

]
