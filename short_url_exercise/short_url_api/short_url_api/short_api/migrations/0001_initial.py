# Generated by Django 4.1.7 on 2023-03-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.CharField(max_length=5000)),
                ('short', models.CharField(max_length=40)),
            ],
        ),
    ]
