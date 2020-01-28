from django.contrib import admin
# from .models import ProductType, Product, Review
from .models import Meeting, MeetingMinutes, Resource, Event

# Register your models here.
# admin.site.register(ProductType)
# admin.site.register(Product)
# admin.site.register(Review)
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)


