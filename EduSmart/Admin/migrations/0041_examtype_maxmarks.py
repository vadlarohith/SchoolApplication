# Generated by Django 5.0.2 on 2024-08-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0040_rename_access_examtype_studentaccess_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examtype',
            name='MaxMarks',
            field=models.IntegerField(null=True),
        ),
    ]
