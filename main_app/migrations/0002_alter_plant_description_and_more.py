# Generated by Django 4.2.10 on 2024-03-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='plant',
            name='watering_frequency',
            field=models.CharField(max_length=100),
        ),
    ]
