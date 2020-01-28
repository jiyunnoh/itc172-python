from django.db import models
#To store the app's users
from django.contrib.auth.models import User

# # Create your models here.
# class ProductType(models.Model):
#     typename = models.CharField(max_length=255)
#     typedescription = models.CharField(max_length=255, nu;;=True, blank=True)
#     #If you do not specify a primary key field, 
#     # django will automatically assign an id autonumbered field as a primary key

#     def __str__(self):
#         return self.typename

#     #The sub class sets some properties for how the class will appear in the db 
#     # and in the ADMIN app.
#     class Meta:
#         #'db_table' sets the table name in postgresql
#         db_table = 'producttype'
#         #'verbose_name_plural' controls how it will be pluralized in the Admin app
#         verbose_name_plural = 'producttypes'

# class Product(models.Model):
#     productname = models.CharField(max_length=255)
#     producttype = models.ForeignKey(ProductType, on_delete = models.DO_NOTHING)
#     user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
#     productprice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
#     productentrydate = models.DateField()
#     producturl = models.URLField(null=True, blank=True)
#     productdescription = models.TextField()

#     def memberdiscount(self):
#         discountpercent = .05
#         return float(self.productprice) * discountpercent

#     def __str__(self):
#         return self.productname

#     class Meta:
#         db_table = 'product'
#         verbose_name_plural = 'products'

# class Review(models.Model):
#     reviewtitle = models.CharField(max_length=255)
#     reviewdate = models.DateField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     #User class which was pre-made by django and exists in the auth library
#     #More than one user can author a review
#     user = models.ManyToManyField(User)
#     reviewrating = models.SmallIntegerField()
#     reviewtext = models.TextField()
    
#     def __str__(self):
#         return self.reviewtitle

#     class Meta:
#         db_table = 'review'
#         verbose_name_plural = 'reviews'


class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    meetinglocation = models.CharField(max_length=255)
    meetingagenda = models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'

class MeetingMinutes(models.Model):
    #How to assign a foreignkey?
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutestext = models.TextField()

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table = 'meetingminutes'
        verbose_name_plural = 'meetingminutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    resourceurl = models.URLField(null='True', blank='Ture')
    dateentered = models.DateField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription = models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'

class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    eventlocation = models.CharField(max_length=255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdescription = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING, null='True')

    def __str__(self):
        return self.eventtitle

    class Meta():
        db_table = 'event'
        verbose_name_plural = 'events'
    




