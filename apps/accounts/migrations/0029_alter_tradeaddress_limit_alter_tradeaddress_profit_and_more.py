# Generated by Django 4.2.4 on 2023-09-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_tradeaddress_ammount_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeaddress',
            name='limit',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='tradeaddress',
            name='profit',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='tradeaddress',
            name='stop_loss',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
        ),
    ]
