from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EventsForm
from .models import Event, UglyEventForm


def events(request):
    events = Event.objects.all()
    request.session["name"] = "andres"
    return render(request, 'events/event_list.html', {'events': events})


def uglyEventsForm(request):
    form = UglyEventForm()
    return render(request, 'events/ugly_event_form.html', {'form': form})


def eventsForm(request):
    if request.method == 'POST':

        form = EventsForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data["fecha"]
            print(request.user.is_authenticated)
            print(request.user.username)
            print(request.user.id)
            evento = Event()

            evento.save()
        return HttpResponseRedirect('/events/eventsForm')
    else:
        form = EventsForm()

    return render(request, 'events/events.html', {'form': form})
