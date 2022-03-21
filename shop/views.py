from django.shortcuts import render, redirect
from .models import Product, User, Order, UUser, Buy
from .forms import OrderForm, AddAddress
from cloudipsp import Api, Checkout
import re
from collections import OrderedDict
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .service import send_regist, send_buy, send_castom


def main_page(request):
    if request.method == 'POST':
        if UUser.objects.get(pk=request.user.id).address != 'Отсутствует':
            search_price = []
            id_buy = []
            for i in OrderedDict(request.POST).items():
                search_price.append(i[1])
                id_buy.append((i[0]))
            api = Api(merchant_id=1396424,
                      secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "BYN",
                "amount": re.sub(r'[.]', '', search_price[1])
            }
            getprod = Product.objects.get(id=id_buy[1])
            url = checkout.url(data).get('checkout_url')
            send_buy(request.user.email, username=request.user, volume=getprod.volume, structure=getprod.structure,
                     flavor=getprod.flavor, price=getprod.price,
                     address=UUser.objects.get(pk=request.user.id).address)
            Buy.objects.create(user_id_id=request.user.id, volume=getprod.volume, structure=getprod.structure,
                               flavor=getprod.flavor, price=getprod.price,
                               address=UUser.objects.get(pk=request.user.id).address)
            return redirect(url)
        else:
            messages.info(request, 'Добавьте адрес доставки!!')
            return redirect('/profile/')
    product = Product.objects.all()
    return render(request, 'shop/index.html', {'product': product})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddAddress(request.POST)
            if form.is_valid():
                UUser.objects.filter(pk=request.user.id).update(address=form.cleaned_data.get('address'))
        return render(request, 'shop/profile.html',
                      {"user": request.user, 'orders': Order.objects.filter(user_id_id=request.user.id),
                       'address': UUser.objects.get(pk=request.user.id).address,
                       'Buy': Buy.objects.filter(user_id_id=request.user.id)})
    return redirect('/login/')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            if User.objects.filter(username=request.POST.get('username')).exists():
                messages.info(request, 'Account already exists')
                return render(request, 'shop/registry.html', {})
            else:
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    send_regist(form.instance.email, form.cleaned_data.get('username'),
                                form.cleaned_data.get('password1'))
                    form.save()
                    messages.success(request, 'Account was created ' + form.cleaned_data.get('username'))
                    return redirect('/login/')
                else:
                    messages.info(request, 'Form not valid')
                    return render(request, 'shop/registry.html', {})
        return render(request, 'shop/registry.html', {})


def logout_user(request):
    logout(request)
    return redirect('/login/')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                messages.info(request, 'Username or Password incorect')
                return render(request, 'shop/login.html', {})

        return render(request, 'shop/login.html', {'request': request})


def catsom_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if UUser.objects.get(pk=request.user.id).address != 'Отсутствует':
            if form.is_valid():
                api = Api(merchant_id=1396424,
                          secret_key='test')
                checkout = Checkout(api=api)
                data = {
                    "currency": "BYN",
                    "amount": 3500,
                }
                send_castom(request.user.email, username=request.user, candle_t=form.cleaned_data.get('candle_t'),
                            candle_color=form.cleaned_data.get('candle_color'),
                            candle_volume=form.cleaned_data.get('candle_volume'),
                            candle_flavor=form.cleaned_data.get('candle_flavor'),
                            address=UUser.objects.get(pk=request.user.id).address)
                Order.objects.create(user_id=request.user, candle_t=form.cleaned_data.get('candle_t'),
                                     candle_color=form.cleaned_data.get('candle_color'),
                                     candle_volume=form.cleaned_data.get('candle_volume'),
                                     candle_flavor=form.cleaned_data.get('candle_flavor'),
                                     address=UUser.objects.get(pk=request.user.id).address)
                return redirect(checkout.url(data).get('checkout_url'))
            else:
                print('#смс что форма невалидна')
                # смс что форма невалидна
                return redirect('/castom/')
        else:
            messages.info(request, 'Добавьте адрес доставки')
            return redirect('/profile/')
    else:
        form = OrderForm()
    return render(request, 'shop/castom.html', {'form': form})
