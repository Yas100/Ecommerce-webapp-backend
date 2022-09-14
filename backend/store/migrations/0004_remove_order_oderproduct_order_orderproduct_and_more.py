# Generated by Django 4.1.1 on 2022-09-13 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_productupdatedat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='oderProduct',
        ),
        migrations.AddField(
            model_name='order',
            name='orderProduct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderProduct', to='store.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderCustomer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrderCustomer', to='store.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderAddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderAddress', to='store.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderMobileNumber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderMobileNumber', to='store.customer'),
        ),
    ]
