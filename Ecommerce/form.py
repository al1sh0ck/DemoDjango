from django import forms
from .models import ContactPage, Blogs, ProductsFullDesc


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

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['name', 'description', 'tags', 'author', 'date', 'views', 'commentsAmount', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'tags': forms.TextInput(attrs={'placeholder': 'Comma-separated tags'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
class ProductFullDescForm(forms.ModelForm):
    class Meta:
        model = ProductsFullDesc
        fields = [
            'name', 'price', 'short_desc', 'width', 'height', 'depth', 'weight',
            'quality_checking', 'freshness_duration', 'when_packeting', 'each_box_contains', 'long_desc', 'image'
        ]
