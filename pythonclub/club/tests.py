from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        meeting = Meeting(meetingtitle = 'JYmeeting')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setup(self):
        meeting = Meeting(meetingtitle = 'Main')
        minutesText = MeetingMinutes(minutestext = 'Main', meetingid = meeting)
        return minutesText  

    def test_string(self):
        minutes = self.setup()
        self.assertEqual(str(minutes), minutes.minutestext)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_string(self):
        res = Resource(resourcename = 'resource1')
        self.assertEqual(str(res), res.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        event = Event(eventtitle = 'event1')
        self.assertEqual(str(event), event.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')