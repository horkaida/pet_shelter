from django.shortcuts import render, redirect
import animals.models
from animals.forms import FeedbackForm
from function_schedule import get_slots, get_calendar
from datetime import datetime, timedelta, date, timezone


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
            form = FeedbackForm(request.POST)
            feedback = form.save(commit=False)
            feedback.user_id_id = request.user.id
            feedback.animal_id_id = animal_id
            feedback.save()
            return redirect("/animals/feedbacks")
        else:
            return redirect("/login")
    else:
        animal = animals.models.Animal.objects.get(id=animal_id)
        animal_feedbacks = animals.models.Feedback.objects.all().filter(animal_id_id=animal_id)
    return render(request, 'animals/animal.html',
                  {"animal": animal, "animal_feedbacks": animal_feedbacks, 'feedback_from': FeedbackForm()})


def get_schedule(request, animal_id):
    duration_options = [1, 2, 3]
    slots = []
    if request.method == 'GET':
        chosen_duration = request.GET.get('duration_options')
        last_calendar_day = get_calendar()[-1]
        chosen_date = request.GET.get('chosen_date')
        if chosen_date:
            date_info = chosen_date.split('-')
            if chosen_duration:
                booked_appointments = (animals.models.Schedule.objects.all()
                                       .filter(animal_id_id=animal_id, start_time__day=int(date_info[2]))
                                       .values_list('start_time', 'end_time'))
                slots = [{'timestamp': slot.timestamp(), "display_date": slot} for slot in
                         get_slots(appointments=list(booked_appointments), chosen_year=int(date_info[0]),
                                   chosen_month=int(date_info[1]), chosen_day=int(date_info[2]),
                                   hours=int(chosen_duration))]
        return render(request, 'animals/schedule.html',
                      {'slots': slots,
                       'duration_options': duration_options,
                       'current_day': date.today(),
                       'last_calendar_day': last_calendar_day,
                       'chosen_date': chosen_date,
                       'chosen_duration': chosen_duration})
    if request.method == 'POST':
        chosen_duration = int(request.POST.get('chosen_duration'))
        start_time = datetime.fromtimestamp(float(request.POST.get('start_time')))
        start_time = start_time.replace(tzinfo=timezone.utc)
        end_time = start_time + timedelta(hours=chosen_duration)
        new_booking = animals.models.Schedule(start_time=start_time,
                                              end_time=end_time,
                                              animal_id_id=animal_id,
                                              user_id_id=request.user.id)
        new_booking.save()
        return render(request, 'animals/success_page.html', {'start_time': start_time, 'end_time': end_time})


def get_all_feedbacks(request):
    types = animals.models.AnimalType.objects.all()
    type_filter = request.GET.get("type")
    if type_filter:
        all_feedbacks = animals.models.Feedback.objects.all().filter(animal_id__animal_type__type=type_filter)
    else:
        all_feedbacks = animals.models.Feedback.objects.all()
    return render(request, 'animals/feedbacks.html', {'feedbacks': all_feedbacks, 'types': types})
