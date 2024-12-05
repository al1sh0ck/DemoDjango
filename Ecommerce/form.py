from django import forms
from .models import ContactPage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = ['name', 'email', 'subject', 'message']  # Fields to include in the form

        # Add placeholders and custom styles to fields
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter Message'
            }),
        }