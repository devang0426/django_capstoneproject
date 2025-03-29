from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Menu

# Home Page View
def home(request):
    return render(request, 'index.html')

# About Page View
def about(request):
    return render(request, 'about.html')

# Booking Page View
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

# Menu Page View
def menu(request):
    menu_items = Menu.objects.all()  # Fetch all menu items
    return render(request, 'menu.html', {'menu_items': menu_items})  # Pass menu_items to the template

# Individual Menu Item Page View
def menu_item(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)  # Fixed variable name
    return render(request, 'menu_item.html', {'menu_item': menu_item})  # Pass correct context variable


