# Generated by Django 3.1.2 on 2020-10-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0004_auto_20201006_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informationmeta',
            name='email',
        ),
        migrations.AddField(
            model_name='informationmeta',
            name='skills',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]