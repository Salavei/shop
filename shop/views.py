from django.shortcuts import render, redirect
from .models import Product, User
from .forms import Registry, LogIn, OrderForm
from django.http import HttpResponseRedirect

from cloudipsp import Api, Checkout
import re
from collections import OrderedDict
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
    if request.method == 'POST':
        form = Registry(request.POST)
        if form.is_valid():
            try:
                print(User.objects.get(email=request.POST.get('email')))
                print('Такого аккаунт уже есть!')
            except User.DoesNotExist:
                print('DoesNotExist')
                User.objects.create(name=request.POST.get('name'), phone=request.POST.get('phone'),
                                    email=request.POST.get('email'), password=request.POST.get('password'))
                return redirect('/')
    return render(request, 'shop/test_registry.html', {})



def login_page(request):
    print(request, 'awdddawdwdawdaw')
    print('request', request.POST)
    if request.method == 'POST':
        print('request', request.POST)
        email = request.POST['email']
        password = request.POST['password']
        return render(request, 'shop/test.html')
    else:
         return render(request, 'shop/test.html')


def catsom_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return HttpResponseRedirect('/')
    else:
        form = OrderForm()
    return render(request, 'shop/castom.html', {'form': form})
