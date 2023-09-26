from django.shortcuts import render

def get_user(request):
    return render(request, 'user/user.html', {})

def get_user_history(request):
    return render(request, 'user/user.html', {})

def login(request):
    return render(request, 'user/user.html', {})

def logout(request):
    return render(request, 'user/user.html', {})

def register(request):
    return render(request, 'user/user.html', {})


