# Generated by Django 3.1 on 2020-09-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200902_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test',
            field=models.TextField(blank=True, null=True),
        ),
    ]