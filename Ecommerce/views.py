from operator import index

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import ContactForm, BlogForm, ProductFullDescForm
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
    products = ShortProd.objects.all()

    # Filtering
    brand = request.GET.get('brand')
    color = request.GET.get('color')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if brand:
        products = products.filter(brand__icontains=brand)  # Add 'brand' field to ShortProd model if needed.
    if color:
        products = products.filter(color__icontains=color)  # Add 'color' field to ShortProd model if needed.
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Sorting
    sort_by = request.GET.get('sort_by', 'name')  # Default sorting by name
    products = products.order_by(sort_by)

    context = {
        'products': products,
    }
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

def single_blog_view(request):
    blog = SingleBlogs.objects.first()  # Or use .get(id=1) if you want a specific blog

    if not blog:
        # Handle the case where no blogs are available, maybe show a 404 or error message
        return render(request, 'karma/single-blog.html')
    images = [img for img in [blog.image1, blog.image2, blog.image3, blog.image4, blog.image5] if img]
    context = {
        'blog': blog,
        'images': images,
    }

    return render(request, 'karma/single-blog.html', context)


def create_blog_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Replace 'blog-list' with your actual blog list URL
        else:
            print("Form errors:", form.errors)  # Debugging for errors
    else:
        form = BlogForm()

    context = {
        'form': form
    }
    return render(request, 'karma/create_blog.html', context)


def create_product_view(request):
    if request.method == 'POST':
        form = ProductFullDescForm(request.POST, request.FILES)
        if form.is_valid():
            product_full = form.save()

            # Automatically create a ShortProd entry
            short_prod = ShortProd.objects.create(
                name=product_full.name,
                price=int(product_full.price),  # Ensure price is an integer
                image=product_full.image
            )

            # Link the ShortProd entry to the ProductsFullDesc entry
            product_full.short_product = short_prod
            product_full.save()

            return redirect('category')  # Replace with your product list view name
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = ProductFullDescForm()

    context = {
        'form': form
    }
    return render(request, 'karma/create_product.html', context)

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
class Tracking(TemplateView):
    template_name = 'karma/tracking.html'
