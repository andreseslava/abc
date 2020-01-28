from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.events),
    url(r'^uglyEventsForm$', views.uglyEventsForm),
    url(r'^eventsForm$', views.eventsForm),
]