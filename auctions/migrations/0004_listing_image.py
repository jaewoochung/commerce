# Generated by Django 3.1.3 on 2020-11-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201123_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]