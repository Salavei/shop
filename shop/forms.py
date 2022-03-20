from django import forms
from .models import Order, UUser
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = UUser
        fields = ['username', 'email', 'phone', 'password1']


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None



class Registry(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)


class LogIn(forms.Form):
    email = forms.EmailField(label='Your email', max_length=100)
    password = forms.CharField(label='Your psw', max_length=100)


TYPE_CHOICES = (
    (1, 'figure'),
    (2, 'candle_standart'),
)
COLOR_CHOICES = (
    (1, 'WHITE'),
    (2, 'YELLOW'),
    (3, 'BLACK'),
)
FLAVOR_CHOICES = (
    (1, 'яблочный пирог'),
    (2, 'черный кокос'),
    (3, 'вечер у камина'),
    (4, 'ягодный пунш'),
    (5, 'сумеречный лес'),
)
VOLUME_CHOICES = (
    (1, '200'),
    (2, '100'),
)
STATUS_CHOICES = (
    (1, 'In processing'),
    (2, 'sent'),
)


class OrderForm(forms.Form):
    candle_t = forms.ChoiceField(choices=TYPE_CHOICES)
    candle_color = forms.ChoiceField(choices=COLOR_CHOICES)
    candle_flavor = forms.ChoiceField(choices=FLAVOR_CHOICES)
    candle_volume = forms.ChoiceField(choices=VOLUME_CHOICES)
