# Generated by Django 4.0.1 on 2023-01-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0015_product_noc'),
    ]

    operations = [
        migrations.CreateModel(
            name='paypal_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('property_cat', models.CharField(max_length=100, null=True)),
                ('property_sel', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
