# Generated by Django 2.2.5 on 2020-07-01 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ponopiza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='itemsname',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
    ]
