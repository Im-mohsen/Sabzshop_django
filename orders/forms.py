from django import forms
from .models import Order


class PhoneVerificationForm(forms.Form):
    phone = forms.CharField(max_length=11, label="شماره تلفن")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 11:
            raise forms.ValidationError("شماره تلفن باید 11 رقمی باشد.")
        return phone


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'postal_code', 'province', 'city']