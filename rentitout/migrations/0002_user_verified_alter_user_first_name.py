# Generated by Django 5.1.1 on 2024-10-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentitout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
