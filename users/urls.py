from django.urls import path
from . import views

urlpatterns = [
    path('register-customer/', views.register_customer, name='register-cutomer'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]