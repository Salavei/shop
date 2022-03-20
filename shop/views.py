from django.shortcuts import render, redirect
from .models import Product, User
from .forms import Registry, OrderForm
from cloudipsp import Api, Checkout
import re
from collections import OrderedDict
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def main_page(request):
    if request.method == 'POST':
        search_price = []
        for i in OrderedDict((request.POST)).items():
            search_price.append(i[1])
        api = Api(merchant_id=1396424,
                  secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "BYN",
            "amount": re.sub(r'[.]', '', search_price[1])
        }
        url = checkout.url(data).get('checkout_url')
        return redirect(url)
    product = Product.objects.all()
    return render(request, 'shop/index.html', {'product': product})


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            qs = User.objects.filter(username=request.POST.get('username'))
            if qs.exists():
                messages.info(request, 'Account already exists')
                return render(request, 'shop/test_registry.html', {})
            else:
                # print(User.objects.filter(username=request.POST.get('username')))
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created ' + user)
                    return redirect('/login/')
                else:
                    messages.info(request, 'Form not valid')
                    return render(request, 'shop/test_registry.html', {})
        return render(request, 'shop/test_registry.html', {})


def logout_user(request):
    logout(request)
    return redirect('/login/')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password incorect')
                return render(request, 'shop/test.html', {})

        return render(request, 'shop/test.html', {'request': request})


def catsom_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return redirect('/')
    else:
        form = OrderForm()
    return render(request, 'shop/castom.html', {'form': form})
