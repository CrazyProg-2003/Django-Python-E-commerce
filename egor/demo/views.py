from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from demo.forms import RegisterUserForm


def login(request):
    return render(request, 'registration/login.html')


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('Login')


def about(request):
        return render(request, 'demo/about.html')


def contact(request):
        return render(request, 'demo/contact.html')


def catalog(request):
        return render(request, 'demo/catalog.html')


def product(request):
        return render(request, 'demo/product.html')


@login_required
def cart(request):
        return render(request, 'demo/cart.html')


@login_required
def checkout(request):
        return render(request, 'demo/checkout.html')


@login_required
def orders(request):
        return render(request, 'demo/orders.html')