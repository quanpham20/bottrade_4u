# Generated by Django 4.2.4 on 2023-09-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_customuser_sell_hi_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="buy_tax",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name="customuser",
            name="sell_tax",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
