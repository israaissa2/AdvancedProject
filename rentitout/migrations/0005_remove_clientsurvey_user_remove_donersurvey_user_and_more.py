# Generated by Django 5.1.1 on 2024-10-28 17:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentitout', '0004_donersurvey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientsurvey',
            name='user',
        ),
        migrations.RemoveField(
            model_name='donersurvey',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verified',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemReservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('total_price', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentitout.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ClientSon',
        ),
        migrations.DeleteModel(
            name='ClientSurvey',
        ),
        migrations.DeleteModel(
            name='DonerSurvey',
        ),
    ]
