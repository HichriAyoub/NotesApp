# Generated by Django 5.0.3 on 2024-03-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]