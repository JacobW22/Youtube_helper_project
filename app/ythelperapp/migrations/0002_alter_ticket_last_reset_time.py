# Generated by Django 4.2.4 on 2023-08-31 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ythelperapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='last_reset_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 30, 22, 0, tzinfo=datetime.timezone.utc)),
        ),
    ]