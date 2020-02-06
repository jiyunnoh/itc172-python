from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getmeetings(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})

def getmeetingminutes(request):
    minutes_list = MeetingMinutes.objects.all()
    return render(request, 'club/minutes.html', {'minutes_list': minutes_list})

def getresources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})    

def getevent(request):
    event_list = Event.objects.all()
    return render(request, 'club/events.html', {'event_list': event_list})

def meetingdetails(request, id):
    meet = get_object_or_404(Meeting, pk=id)
    minutes = MeetingMinutes.objects.filter(meetingid=id).count()
    context = {
        'meet': meet,
        'minutes': minutes,
    } 
    return render(request, 'club/meetingdetails.html', context = context)
