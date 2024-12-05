from django.shortcuts import render
from django.http import HttpResponse

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