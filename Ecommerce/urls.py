from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import single_blog_view

urlpatterns = [
    path('', lambda request: redirect('contact/')),  # Redirect root URL to 'contact/'
    path('contact/', views.contact_view, name='contact'),  # URL path is 'contact/'
    path('cart/', views.Cart.as_view(), name='cart'),
    path('category/', views.category_view, name='category'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('confirmation/', views.Confirmation.as_view(), name='confirmation'),
    path('elements/', views.Elements.as_view(), name='elements'),
    path('index/', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('single-blog/', single_blog_view, name='single-blog'),
    path('single-product/', views.singprod, name='single-product'),
    path('blog/', views.blogs_view, name='blog'),
    path('tracking/', views.Tracking.as_view(), name='tracking'),
    path('create-blog/', views.create_blog_view, name='create-blog'),
    path('create-product/', views.create_product_view, name='create-product'),



] + staticfiles_urlpatterns()