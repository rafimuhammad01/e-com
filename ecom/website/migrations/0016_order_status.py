# Generated by Django 3.1 on 2020-09-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200903_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('waiting_for_payment', 'Waiting for Payment'), ('verified', 'Verified'), ('on_shipping', 'On Shipping'), ('arrived', 'Arrived'), ('finish', 'Finish')], default='waiting_for_payment', max_length=64),
        ),
    ]
