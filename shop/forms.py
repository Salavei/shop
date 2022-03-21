from django import forms
from .models import Order, UUser
from django.contrib.auth.forms import UserCreationForm


class AddAddress(forms.Form):
    address = forms.CharField(max_length=255)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = UUser
        fields = ['username', 'email', 'phone', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None


TYPE_CHOICES = (
    ('фигура', 'фигура'),
    ('стандартная', 'стандартная'),
)
COLOR_CHOICES = (
    ('белый', 'белый'),
    ('желтый', 'желтый'),
    ('черный', 'черный'),
)
FLAVOR_CHOICES = (
    ('яблочный пирог', 'яблочный пирог'),
    ('черный кокос', 'черный кокос'),
    ('вечер у камина', 'вечер у камина'),
    ('ягодный пунш', 'ягодный пунш'),
    ('сумеречный лес', 'сумеречный лес'),
)
VOLUME_CHOICES = (
    (200, 200),
    (100, 100),
)


class OrderForm(forms.Form):
    candle_t = forms.ChoiceField(choices=TYPE_CHOICES)
    candle_color = forms.ChoiceField(choices=COLOR_CHOICES)
    candle_volume = forms.ChoiceField(choices=VOLUME_CHOICES)
    candle_flavor = forms.ChoiceField(choices=FLAVOR_CHOICES)
