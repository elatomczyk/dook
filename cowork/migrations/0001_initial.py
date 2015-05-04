# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('vat_id', models.CharField(default='000-000-000-000', max_length=35)),
                ('website', models.URLField(max_length=50)),
                ('logo', models.ImageField(upload_to=b'')),
                ('user', models.ForeignKey(related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rent_start_date', models.DateTimeField(null=True)),
                ('rent_end_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=200)),
                ('total_desks', models.IntegerField(verbose_name='Total desks')),
                ('reserved_desks', models.IntegerField(verbose_name='Reserved desks')),
                ('price', models.DecimalField(verbose_name='Price per desk $', max_digits=12, decimal_places=2)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(default='00-000', max_length=5)),
                ('company', models.ForeignKey(related_name='locations', to='cowork.Company')),
            ],
        ),
        migrations.AddField(
            model_name='desk',
            name='location',
            field=models.OneToOneField(related_name='desks', to='cowork.Location'),
        ),
        migrations.AddField(
            model_name='desk',
            name='owner',
            field=models.OneToOneField(related_name='desks', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
