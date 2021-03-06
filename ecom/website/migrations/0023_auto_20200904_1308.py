# Generated by Django 3.1 on 2020-09-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20200904_1228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='ProductOrder',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='website.ProductOrder'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='M94A4GQP', max_length=50, primary_key=True, serialize=False),
        ),
    ]
