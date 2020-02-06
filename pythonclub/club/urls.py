from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.getmeetings, name='meetings'),
    path('minutes/', views.getmeetingminutes, name='minutes'),
    path('resources/', views.getresources, name='resources'),
    path('events/', views.getevent, name='events'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
]