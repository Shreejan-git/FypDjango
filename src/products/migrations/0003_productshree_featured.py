# Generated by Django 2.0.7 on 2020-06-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200611_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='productshree',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
