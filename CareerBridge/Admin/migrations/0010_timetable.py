# Generated by Django 5.0.2 on 2024-07-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_teacher_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=10)),
                ('Image', models.ImageField(upload_to='timetable')),
            ],
        ),
    ]
