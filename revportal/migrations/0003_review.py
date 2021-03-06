# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revportal', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=60)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revportal.Post')),
            ],
        ),
    ]
