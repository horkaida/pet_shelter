from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import animals.models
from animals.models import Schedule

def get_user(request):
    return render(request, 'user/user.html')

def get_user_history(request):
    if request.user.is_authenticated:
        all_appointments = animals.models.Schedule.objects.all().filter(user_id_id=request.user.id)
        return render(request, 'user/user_history.html', {'all_appointments':all_appointments})
    else:
        return redirect('/login')

def log_in(request):
    if request.method=='GET':
        return render(request, 'user/login.html')
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user')
        else:
            return render(request, 'user/login.html', {'error':'Неправильні дані!'})
def log_out(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')

def register(request):
    if request.method=='GET':
        return render(request, 'user/registration.html')
    if request.method=='POST':
        if request.POST.get('password') == request.POST.get('repeat_password'):
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'))
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            return redirect('/login')
        else:
            return render(request, 'user/registration.html', {'error':'Паролі не співпадають.'})


