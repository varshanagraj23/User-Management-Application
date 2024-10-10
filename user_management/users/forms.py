from django import forms
from .models import UserDetail

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

    # Custom validation for phone number
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) < 10:
            raise forms.ValidationError('Enter a valid 10-digit phone number.')
        return phone_number

    # Custom validation for email (if any further than unique is required)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserDetail.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
