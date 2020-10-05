# Generated by Django 3.1.2 on 2020-10-05 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('languages', models.CharField(max_length=512, verbose_name='langs')),
                ('tools', models.CharField(max_length=512, verbose_name='tools')),
                ('homepage', models.CharField(max_length=256)),
                ('screen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_lang', models.CharField(max_length=5)),
                ('keywords', models.CharField(max_length=512, verbose_name='tools')),
                ('description', models.TextField(max_length=2048)),
                ('project_meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectmeta')),
            ],
        ),
    ]
