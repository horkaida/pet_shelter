from django.shortcuts import render

def main_page(request):
    return render(request, 'index.html', {})

def get_our_contacts(request):
    return render(request, 'user/user.html', {})