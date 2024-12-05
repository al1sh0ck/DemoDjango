from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', lambda request: redirect('contact/')),  # Redirect root URL to 'contact/'
    path('contact/', views.contact_view, name='contact'),  # URL path is 'contact/'
    path('blog/', views.Blog.as_view(), name='blog'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('category/', views.Category.as_view(), name='category'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('confirmation/', views.Confirmation.as_view(), name='confirmation'),
    path('elements/', views.Elements.as_view(), name='elements'),
    path('index/', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('single-blog/', views.Singleblog.as_view(), name='single-blog'),
    path('single-product/', views.Singleproduct.as_view(), name='single-product'),
    path('tracking/', views.Tracking.as_view(), name='tracking'),



] + staticfiles_urlpatterns()