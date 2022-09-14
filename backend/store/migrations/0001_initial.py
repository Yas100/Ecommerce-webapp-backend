# Generated by Django 4.1.1 on 2022-09-13 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobileNumber', models.IntegerField(blank=True, null=True)),
                ('alternateMobileNumber', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('productAddedAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('productUpdatedAt', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('orderPrice', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('orderCreatedAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('OrderCustomer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrderCustomer', to='store.customer')),
                ('oderProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('orderAddress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderAddress', to='store.customer')),
                ('orderMobileNumber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderMobileNumber', to='store.customer')),
            ],
        ),
    ]