# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-05 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('locality', models.CharField(choices=[('D', 'Domestic'), ('I', 'Import')], max_length=1)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Brewery'),
        ),
    ]