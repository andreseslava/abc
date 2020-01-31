from datetime import datetime


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EventsForm
from .models import Event


@login_required
def events(request):
    form = EventsForm()
    events = Event.objects.filter(author=request.user).order_by('created_At')
    if request.method == 'POST':
        print("post")
        return HttpResponseRedirect('/events')
    else:
        form = EventsForm()
    return render(request, 'events/events.html', {'events': events, 'form': form})


@login_required
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


@login_required
def delete(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        print(id)
        Event.objects.filter(id=id).delete()
        return HttpResponseRedirect('/events')
    else:
        form = EventsForm()
    return render(request, 'events/events.html')


@login_required
def edit(request):
    form = EventsForm()
    id = request.GET.get("id")
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            #id = request.POST.get("id")
            print(id)
            event = Event.objects.filter(id=id)
            event.name = form.cleaned_data['name']
            event.address = form.cleaned_data['address']
            event.place = form.cleaned_data['place']
            event.startDate = datetime.now()
            event.endDate = datetime.now()
            event.description = form.cleaned_data['description']
            event.author = request.user
            event.update()
        return HttpResponseRedirect('/events')

    return render(request, 'events/events_edit_form.html', {'form': form, 'id': id})
