# Generated by Django 5.1.1 on 2024-10-15 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentitout', '0003_clientsurvey_clientson'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonerSurvey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('third_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('id_number', models.CharField(max_length=9)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('marital_status', models.CharField(max_length=50)),
                ('number_of_family_members', models.IntegerField(default=0)),
                ('phone_number', models.CharField(max_length=13)),
                ('academic_qualification', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('place_of_work', models.CharField(max_length=200)),
                ('number_of_sons', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('has_accepted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
