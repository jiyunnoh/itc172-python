from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, gettypes, getproducts
from django.urls import reverse
from django.contrib.auth.models import User

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

class New_Product_authentication_test(TestCase):
    def setup(self):
        self.test_user = User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meet = Meeting.objects.create(meetingname='testmeeting1')
        self.resrc = Resource.objects.create(resourcename='testresrc1', resourcetype='resrctype1')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')
    
    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newmeeting.html')