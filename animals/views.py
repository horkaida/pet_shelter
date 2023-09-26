from django.shortcuts import render

def get_all_animals(request):
    return render(request, 'animals/animals.html', {})

def get_animal(request):
    return render(request, 'animals/animals.html', {})

def get_schedule(request):
    return render(request, 'animals/animals.html', {})
