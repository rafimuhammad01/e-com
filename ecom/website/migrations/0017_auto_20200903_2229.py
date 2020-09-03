# Generated by Django 3.1 on 2020-09-03 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='UGONOF1G', max_length=50, primary_key=True, serialize=False),
        ),
    ]