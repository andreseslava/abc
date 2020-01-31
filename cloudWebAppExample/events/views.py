from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EventsForm
from .models import Event


def events(request):
    form = EventsForm()
    events = Event.objects.filter(author=request.user)
    if request.method == 'POST':
        print("post")
        return HttpResponseRedirect('/events')
    else:
        form = EventsForm()
    return render(request, 'events/events.html', {'events': events, 'form': form})


def eventsForm(request):

    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            event = Event()
            event.name = form.cleaned_data['name']
            event.address = form.cleaned_data['address']
            event.place = form.cleaned_data['place']
            event.startDate = datetime.now()
            event.endDate = datetime.now()
            event.description = form.cleaned_data['description']
            event.author = request.user
            event.save()
        return HttpResponseRedirect('/events')
    else:
        form = EventsForm()

    return render(request, 'events/events_form.html', {'form': form})


def delete(request):
    if request.method == 'POST':
        id=request.POST.get("id")
        print(id)
        Event.objects.filter(id=id).delete()
        return HttpResponseRedirect('/events')
    else:
        form = EventsForm()
    return render(request, 'events/events.html')