# Generated by Django 3.1 on 2020-09-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200901_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, max_length=1),
        ),
    ]
