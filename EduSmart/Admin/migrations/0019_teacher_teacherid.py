# Generated by Django 5.0.2 on 2024-07-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_teacher_classteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='TeacherID',
            field=models.CharField(default='1', max_length=10),
            preserve_default=False,
        ),
    ]
