# Generated by Django 3.1.2 on 2020-10-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0002_informationmeta_email_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationmeta',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]