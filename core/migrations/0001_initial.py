# Generated by Django 4.1.3 on 2022-11-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, null=True, unique=True)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]