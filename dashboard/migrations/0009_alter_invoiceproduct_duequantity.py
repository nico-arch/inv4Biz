# Generated by Django 3.2.5 on 2021-07-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_customer_funds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceproduct',
            name='dueQuantity',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Due Qtty'),
        ),
    ]
