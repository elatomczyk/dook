from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_unicode


class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=35, default='000-000-000-000')
    website = models.URLField(max_length=50)
    logo = models.ImageField()

    def __unicode__(self):
        return smart_unicode(" ".join([self.name, str(self.logo)]))


class Location(models.Model):
    company = models.ForeignKey('Company',
        related_name='locations')
    city = models.CharField(max_length=200)
    total_desks = models.IntegerField(verbose_name='Total desks')
    reserved_desks = models.IntegerField(verbose_name='Reserved desks')
    price = models.DecimalField(verbose_name='Price per desk $',
        max_digits=12, decimal_places=2)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=5, default='00-000')

    def __unicode__(self):
        return '%s' % (self.city)

    @property
    def free_desks(self):
        return self.total_desks - self.reserved_desks


class Desk(models.Model):
    owner = models.OneToOneField('accounts.User', related_name='desks',
        null=True)
    location = models.OneToOneField(Location, related_name='desks')
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return '%s' % self.location
