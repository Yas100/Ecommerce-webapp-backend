# Generated by Django 4.1.1 on 2022-09-17 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_orderprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='OrderCustomer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderAddress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderMobileNumber',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]