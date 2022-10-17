from demo.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
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
        cart_item = request.user.cart_set.all()
        return render(request, 'demo/cart.html',
                      context={'cart_item': cart_item})


@login_required
def checkout(request):
        return render(request, 'demo/checkout.html')


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'demo/orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date')


@login_required
def orders(request):
        return render(request, 'demo/orders.html')


@login_required
def delete_order(request, pk):
    order = Order.objects.filter(user=request.user, pk=pk)
    if order:
        order.delete()
    return redirect('orders')