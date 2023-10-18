from django.shortcuts import render
from django.contrib.auth.models import User

def main_page(request):
    return render(request, 'index.html', {})

def get_our_contacts(request):
    return render(request, 'user/user.html', {})