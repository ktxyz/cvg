# Generated by Django 3.1.2 on 2020-10-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationmeta',
            name='email_href',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
