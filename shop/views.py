from django.shortcuts import render, redirect
from .models import Product, User, Order, UUser
from .forms import OrderForm, AddAddress
from cloudipsp import Api, Checkout
import re
from collections import OrderedDict
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def main_page(request):
    if request.method == 'POST':
        if UUser.objects.get(pk=request.user.id).address != 'Отсутствует':
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
            # Добавлять тут таск на покупку сс адресом доставки
            return redirect(url)
        else:
            # смс чтобы адрес добавили
            return redirect('/profile/')
    product = Product.objects.all()
    return render(request, 'shop/index.html', {'product': product})


def profile(request):
    if request.user.is_authenticated:
        # qs = Order.objects.get(user_id=request.user.id)
        if request.method == 'POST':
            form = AddAddress(request.POST)
            if form.is_valid():
                UUser.objects.filter(pk=request.user.id).update(address=form.cleaned_data.get('address'))

        return render(request, 'shop/profile.html', {"user": request.user, 'orders': 'dwd', 'address': UUser.objects.get(pk=request.user.id).address})
    return redirect('/login/')


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
                return redirect('/profile/')
            else:
                messages.info(request, 'Username or Password incorect')
                return render(request, 'shop/test.html', {})

        return render(request, 'shop/test.html', {'request': request})


def catsom_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(UUser.objects.get(pk=request.user.id).address)
        if UUser.objects.get(pk=request.user.id).address != 'Отсутствует':
            if form.is_valid():
                api = Api(merchant_id=1396424,
                          secret_key='test')
                checkout = Checkout(api=api)
                data = {
                    "currency": "BYN",
                    "amount": 3500,
                }
                url = checkout.url(data).get('checkout_url')
                Order.objects.create(user_id=request.user, candle_t=form.cleaned_data.get('candle_t'),
                                     candle_color=form.cleaned_data.get('candle_color'),
                                     candle_volume=form.cleaned_data.get('candle_volume'),
                                     candle_flavor=form.cleaned_data.get('candle_flavor'),address=UUser.objects.get(pk=request.user.id).address)
                return redirect(url)
            else:
                #смс что форма невалидна
                return redirect('/castom/')
        else:
            messages.info(request, 'Добавьте адрес доставки')
            return redirect('/profile/')
    else:
        form = OrderForm()
    return render(request, 'shop/castom.html', {'form': form})
