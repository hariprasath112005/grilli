from django.shortcuts import render
from django.contrib import messages
from .forms import TableForm, EmailForm

# Create your views here.
def index(request):
    if request.method =="POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            form.save()
         
            messages.info(request, "Booking Submitted")
        
        else:
            form = EmailForm()

    return render(request, 'index.html')

def book_table(request):
    if request.method =="POST":
        form = TableForm(request.POST)

        if form.is_valid():
            form.save()
         
            messages.info(request, "Booking Submitted")
        
        else:
            form = TableForm()

    return render(request, 'book_table.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')