# Generated by Django 4.2.6 on 2024-12-17 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('email_id', models.EmailField(max_length=100, unique=True)),
                ('phone_no', models.CharField(max_length=15, null=True)),
                ('phone_code', models.CharField(default='91', max_length=10)),
                ('password', models.CharField(max_length=100, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofilestatus')),
            ],
        ),
    ]
