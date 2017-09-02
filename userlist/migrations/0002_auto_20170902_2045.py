# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='location',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='repo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repolist.Repo'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='user_type',
            field=models.CharField(max_length=16, null=True),
        ),
    ]