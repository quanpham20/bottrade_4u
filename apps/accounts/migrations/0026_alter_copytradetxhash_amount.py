# Generated by Django 4.2.4 on 2023-09-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_copytradetxhash_token_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copytradetxhash',
            name='amount',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
        ),
    ]
