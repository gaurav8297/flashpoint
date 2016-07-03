# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import facemash.models


class Migration(migrations.Migration):

    dependencies = [
        ('facemash', '0007_auto_20160630_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='rank_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_a', models.IntegerField()),
                ('id_b', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='total_likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('t_l', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='rd',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='sigma',
        ),
        migrations.AddField(
            model_name='photo',
            name='Discription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='Name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='height_field',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=facemash.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='photo',
            name='nlikes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='width_field',
            field=models.IntegerField(default=1000),
        ),
    ]
