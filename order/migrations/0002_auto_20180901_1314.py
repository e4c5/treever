# Generated by Django 2.0 on 2018-09-01 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billingAddress1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingCity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingCountry',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingPostcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingAddress1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingCity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingCountry',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingPostcode',
        ),
    ]