# Generated by Django 4.2.10 on 2024-03-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('watering_frequency', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
    ]
