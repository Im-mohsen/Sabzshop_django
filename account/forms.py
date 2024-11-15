from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ShopUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm


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


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label="رمز عبور")
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput, label="تکرار رمز عبور")

    class Meta:
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("رمز عبورها باهم یکسان نیستند!")
        return cd['password2']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if ShopUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("phone already exists!")
        return phone


class UserEditForm(forms.ModelForm):
    class Meta:
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name', 'address']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if ShopUser.objects.exclude(id=self.instance.id).filter(phone=phone).exists():
            raise forms.ValidationError("phone already exists!")
        return phone


class CustomPasswordChangeForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)