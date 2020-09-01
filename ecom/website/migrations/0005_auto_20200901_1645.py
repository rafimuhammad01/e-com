# Generated by Django 3.1 on 2020-09-01 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200901_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.review'),
        ),
    ]
