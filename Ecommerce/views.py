from operator import index

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import ContactForm
from .models import ContactPage
from django import forms
# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Bind form with submitted data
        if form.is_valid():
            form.save()  # Save form data to the database
            return HttpResponse("Thank you for your message!")  # Redirect or display success message
    else:
        form = ContactForm()  # Render an empty form for GET request

    return render(request, 'karma/contact.html', {'form': form})

class Blog(TemplateView):
    template_name = 'karma/Blog.html'
class Cart(TemplateView):
    template_name = 'karma/cart.html'
class Category(TemplateView):
    template_name = 'karma/category.html'
class Checkout(TemplateView):
    template_name = 'karma/checkout.html'
class Confirmation(TemplateView):
    template_name = 'karma/confirmation.html'
class Elements(TemplateView):
    template_name = 'karma/elements.html'
class Index(TemplateView):
    template_name = 'karma/index.html'
class Login(TemplateView):
    template_name = 'karma/login.html'
class Singleblog(TemplateView):
    template_name = 'karma/single-blog.html'
class Singleproduct(TemplateView):
    template_name = 'karma/single-product.html'
class Tracking(TemplateView):
    template_name = 'karma/tracking.html'
