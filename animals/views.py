from django.shortcuts import render, redirect
import animals.models


def get_all_animals(request):
    types = animals.models.AnimalType.objects.all()
    type_filter = request.GET.get("type")
    if type_filter:
        animal_list = animals.models.Animal.objects.all().filter(animal_type__type=type_filter)
    else:
        animal_list = animals.models.Animal.objects.all()
    all_feedbacks = animals.models.Feedback.objects.all().order_by('-id')[:5]
    return render(request, 'animals/animals.html',
                  {"animal_list": animal_list, "all_feedbacks": all_feedbacks, 'types': types})


def get_animal(request, animal_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            new_feedback = animals.models.Feedback(title=request.POST['title'],
                                                   text=request.POST['text'],
                                                   animal_id_id=request.POST['animal_id'],
                                                   user_id_id=1)
            new_feedback.save()
            return redirect("/animals/feedbacks")
        else:
            return redirect("/login")
    else:
        animal = animals.models.Animal.objects.get(id=animal_id)
        animal_feedbacks = animals.models.Feedback.objects.all().filter(animal_id_id=animal_id)
        return render(request, 'animals/animal.html', {"animal": animal, "animal_feedbacks": animal_feedbacks})


def get_schedule(request):
    return render(request, 'animals/animals.html', {})


def get_all_feedbacks(request):
    types = animals.models.AnimalType.objects.all()
    type_filter = request.GET.get("type")
    if type_filter:
        all_feedbacks = animals.models.Feedback.objects.all().filter(animal_id__animal_type__type=type_filter)
    else:
        all_feedbacks = animals.models.Feedback.objects.all()
    return render(request, 'animals/feedbacks.html', {'feedbacks': all_feedbacks, 'types': types})
