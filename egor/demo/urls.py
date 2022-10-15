from .views import *
from demo import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views.login),
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('', catalog, name='catalog'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('product/<pk>', product, name='product'),

    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('orders', orders, name='orders'),
]