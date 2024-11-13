from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ShopUser
from django.contrib.auth.forms import AuthenticationForm


class ShopUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_staff', 'is_active', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Phone already exists.')
        else:
            if ShopUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('Phone already exists.')

        if not phone.isdigit():
            raise forms.ValidationError('Phone must be a number.')

        if not phone.startswith('09'):
            raise forms.ValidationError('Phone must start with 09.')

        if len(phone) != 11:
            raise forms.ValidationError('Phone must have 11 digits.')

        return phone


class ShopUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_staff', 'is_active', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Phone already exists.')
        else:
            if ShopUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('Phone already exists.')

        if not phone.isdigit():
            raise forms.ValidationError('Phone must be a number.')

        if not phone.startswith('09'):
            raise forms.ValidationError('Phone must start with 09.')

        if len(phone) != 11:
            raise forms.ValidationError('Phone must have 11 digits.')

        return phone


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, required=True)
    password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)
