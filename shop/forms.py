from django import forms
from .models import UUser
from .models import TYPE_CHOICES, COLOR_CHOICES, FLAVOR_CHOICES, VOLUME_CHOICES
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


class OrderForm(forms.Form):
    candle_t = forms.ChoiceField(choices=TYPE_CHOICES)
    candle_color = forms.ChoiceField(choices=COLOR_CHOICES)
    candle_volume = forms.ChoiceField(choices=VOLUME_CHOICES)
    candle_flavor = forms.ChoiceField(choices=FLAVOR_CHOICES)
