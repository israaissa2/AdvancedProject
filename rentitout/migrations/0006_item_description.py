# Generated by Django 5.1.1 on 2024-10-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentitout', '0005_remove_clientsurvey_user_remove_donersurvey_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
