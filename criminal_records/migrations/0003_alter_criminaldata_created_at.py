# Generated by Django 4.2.19 on 2025-03-24 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminal_records', '0002_criminaldata_assigned_to_criminaldata_c_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminaldata',
            name='created_at',
            field=models.DateField(db_column='Created_At', default=datetime.date(2025, 3, 25)),
        ),
    ]
