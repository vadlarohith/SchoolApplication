# Generated by Django 5.0.2 on 2024-07-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_remove_student_fathername_remove_student_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('MobileNo', models.CharField(max_length=10)),
            ],
        ),
    ]
