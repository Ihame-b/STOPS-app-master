# Generated by Django 4.1.3 on 2022-11-10 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0020_cartproduct_cargo1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='cargo1',
        ),
    ]
