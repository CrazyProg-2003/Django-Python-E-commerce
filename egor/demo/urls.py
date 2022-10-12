from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views.login),
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
]