from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.events),
    url(r'^eventsform$', views.eventsForm),
    url(r'^delete', views.delete),
    url(r'^edit', views.edit),
]