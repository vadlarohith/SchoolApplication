# Generated by Django 5.0.2 on 2024-07-25 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0021_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalFee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TotalPaidAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DueAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('NowPaidAmount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.student')),
            ],
        ),
    ]
