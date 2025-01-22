from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('normal-user/', views.normal_user_home, name='normal_user_home'),
    path('hotel-admin/', views.hotel_admin_dashboard, name='hotel_admin_dashboard'),
    path('main-admin/', views.main_admin_dashboard, name='main_admin_dashboard'),
    path('', views.signup_view, name='home'),
]
