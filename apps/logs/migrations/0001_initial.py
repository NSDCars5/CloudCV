# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 08:36
from __future__ import unicode_literals

import base.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('log_type', models.CharField(choices=[('Submission', 'Submission'), ('Break', 'Break')], max_length=30)),
                ('demo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demos.Demo')),
            ],
            options={
                'db_table': 'demo_logs',
            },
        ),
        migrations.CreateModel(
            name='LogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default=False, upload_to=base.utils.RandomFileName('demo_log_images'))),
                ('image_type', models.CharField(choices=[('Input', 'Input'), ('Output', 'Output')], max_length=10)),
                ('demo_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.DemoLog')),
            ],
            options={
                'db_table': 'log_images',
            },
        ),
        migrations.CreateModel(
            name='LogText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=50)),
                ('text_type', models.CharField(choices=[('Input', 'Input'), ('Output', 'Output')], max_length=10)),
                ('demo_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.DemoLog')),
            ],
            options={
                'db_table': 'log_texts',
            },
        ),
    ]