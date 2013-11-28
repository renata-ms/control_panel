from django.db import models
from library.models import Book
import datetime


# Create your models here.
class Order(models.Model):

    itemld = models.ForeignKey('Book')
    created = models.DateField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.itemld


class Customer(models.Model):

    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    address = models.TextField()

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.firstName, self.lastName, self.address)
