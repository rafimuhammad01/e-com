# Generated by Django 3.1 on 2020-09-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200901_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='website.Review'),
        ),
    ]