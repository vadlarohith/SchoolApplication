# Generated by Django 5.0.2 on 2024-07-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0021_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeDetailsForClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=10)),
                ('Fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
