from django.shortcuts import render
from django.contrib import messages
from .forms import TableForm, EmailForm

# Create your views here.
def index(request):
    if request.method =="POST":
        # Forms are handled by Netlify Forms
        messages.info(request, "Subscription Submitted")
    return render(request, 'index.html')

def book_table(request):
    if request.method =="POST":
        # Forms are handled by Netlify Forms
        messages.info(request, "Booking Submitted")
    return render(request, 'book_table.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')