# Generated by Django 4.2.4 on 2023-09-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_customuser_buy_tax_customuser_sell_tax"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="max_gas",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
