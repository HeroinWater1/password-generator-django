from django.shortcuts import render
from random import choice
from string import ascii_lowercase, ascii_uppercase

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    ascii_letters=ascii_lowercase

    password = ''

    if request.GET.get('uppercase'):
        ascii_letters+=ascii_uppercase
    if request.GET.get('numbers'):
        ascii_letters+='0123456789'
    if request.GET.get('special'):
        ascii_letters+='!@#$%^&*(){}/:""\''
    
    lenght = int(request.GET.get('lenght', 12))

    for i in range(lenght):
        password+=choice(ascii_letters)

    return render(request, 'generator/password.html', {'password':password})

def aboutus(request):
    return render(request, 'generator/about.html')
    
def contact(request):
    return render(request, 'generator/contact.html')