# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bfeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buddyResponse', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='mfeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentorResponse', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='userName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='mfeedback',
            name='mentorName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback_app.userName'),
        ),
        migrations.AddField(
            model_name='bfeedback',
            name='buddyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback_app.userName'),
        ),
    ]
