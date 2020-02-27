from django import forms
from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

class ResourceForm(forms.ModelForm):
    class Meta: 
        model = Resource
        fields = '__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'

class Meeting_Form_Test(TestCase):
    def test_meetingform_is_valid(self):
        form = MeetingForm(data={'meetingtitle': "title1", 'meetinglocation': "AR"})
        self.assertTrue(form.is_valid())

    def test_meetingform_minus_location(self):
        form = MeetingForm(data={'meetingtitle': "title1"})
        self.assertTrue(form.is_valid())

    def test_meetingform_empty(self):
        form = MeetingForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())

class Resource_Form_Test(TestCase):
    def test_resourceform_is_valid(self):
        form = ResourceForm(data={'resourcename': "name1", 'resourcetype': "type1"})
        self.assertTrue(form.is_valid())

    def test_resourceform_minus_type(self):
        form = ResourceForm(data={'resourcename': "name1"})
        self.assertTrue(form.is_valid())

    def test_resourceform_empty(self):
        form = ResourceForm(data={'resourcename': ""})
        self.assertFalse(form.is_valid())


