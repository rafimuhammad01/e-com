# Generated by Django 3.1 on 2020-08-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_customer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email_verication_key',
            field=models.CharField(default='asal', max_length=5),
            preserve_default=False,
        ),
    ]
