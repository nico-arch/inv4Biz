# Generated by Django 3.2.5 on 2021-07-05 15:48

import datetime
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True, unique=True)),
                ('email', models.EmailField(default='default@default.com', max_length=254, null=True)),
                ('phone', models.PositiveIntegerField(default=0, null=True)),
                ('address', models.CharField(default='--------', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_backup', models.CharField(max_length=500, null=True)),
                ('email_backup', models.EmailField(max_length=254, null=True)),
                ('phone_backup', models.PositiveIntegerField(null=True)),
                ('address_backup', models.CharField(max_length=500, null=True)),
                ('PaymentType', models.CharField(choices=[('Cash', 'Cash'), ('Check', 'Check'), ('Credit', 'Credit')], max_length=50, null=True, verbose_name='Payment Type')),
                ('Date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Date')),
                ('Total', models.FloatField(default=0.0, null=True)),
                ('discount', models.FloatField(default=0.0, null=True, verbose_name='Discount')),
                ('currency', models.CharField(choices=[('HTG', 'HTG')], default='HTG', max_length=50, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.customer')),
            ],
            options={
                'ordering': ('Date',),
            },
        ),
        migrations.CreateModel(
            name='ModelCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True, unique=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.category')),
            ],
        ),
        migrations.CreateModel(
            name='Proforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_backup', models.CharField(max_length=500, null=True)),
                ('email_backup', models.EmailField(max_length=254, null=True)),
                ('phone_backup', models.PositiveIntegerField(null=True)),
                ('address_backup', models.CharField(max_length=500, null=True)),
                ('Date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Date')),
                ('Total', models.FloatField(default=0.0, null=True)),
                ('discount', models.FloatField(default=0.0, null=True, verbose_name='Discount')),
                ('currency', models.CharField(choices=[('HTG', 'HTG')], default='HTG', max_length=50, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.customer')),
            ],
            options={
                'ordering': ('Date',),
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProformaProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=500, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('Total', models.FloatField(null=True)),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.product')),
                ('Proforma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.proforma')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=500, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('Total', models.FloatField(null=True)),
                ('Invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.invoice')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.product')),
            ],
        ),
    ]
