from operator import index

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import ContactForm
from .models import ContactPage, ShortProd, ProductsFullDesc, Blogs, SingleBlogs
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

def category_view(request):
    products = ShortProd.objects.all()[:6]
    context = {'products': products}
    return render(request, 'karma/category.html', context)

def singprod(request):
    product = ProductsFullDesc.objects.all()[0]
    context = {'product': product}
    return render(request, 'karma/single-product.html', context)

def blogs_view(request):
    blogs = Blogs.objects.all()
    context = {'blogs': blogs}
    for blog in blogs:
        blog.split_tags = blog.tags.split(',')  # Preprocess tags as a list
    return render(request, 'karma/blog.html', context)

class Cart(TemplateView):
    template_name = 'karma/cart.html'
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
class Tracking(TemplateView):
    template_name = 'karma/tracking.html'
