# Generated by Django 5.0.2 on 2024-08-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0027_remove_attendence_month_attendence_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='Date',
        ),
        migrations.AddField(
            model_name='attendence',
            name='Month',
            field=models.CharField(default='January', max_length=10),
            preserve_default=False,
        ),
    ]
