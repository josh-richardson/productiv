# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 11:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useful', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='userwebsite',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Website'),
        ),
        migrations.AddField(
            model_name='userwebsite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.UserProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sites',
            field=models.ManyToManyField(through='backend.UserWebsite', to='backend.Website'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
