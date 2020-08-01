# Generated by Django 2.2.5 on 2020-07-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponopiza', '0004_auto_20200701_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='placedorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderuser', models.CharField(max_length=64)),
                ('ordername', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='placedtoppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordertoppingname', models.CharField(max_length=64)),
                ('order', models.ManyToManyField(blank=True, related_name='placedtoppings', to='ponopiza.placedorders')),
            ],
        ),
    ]
