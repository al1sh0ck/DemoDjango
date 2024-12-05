from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', lambda request: redirect('contact/')),  # Redirect root URL to 'contact/'
    path('contact/', views.contact_view, name='contact'),  # URL path is 'contact/'


] + staticfiles_urlpatterns()