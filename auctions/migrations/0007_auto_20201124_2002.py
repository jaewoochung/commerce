# Generated by Django 3.1.3 on 2020-11-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20201124_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
