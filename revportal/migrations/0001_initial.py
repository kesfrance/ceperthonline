# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-12 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.TextField()),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('views', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]