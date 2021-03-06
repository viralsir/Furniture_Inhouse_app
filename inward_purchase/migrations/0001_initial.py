# Generated by Django 3.2.4 on 2021-07-05 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prodinward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inward_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.utcnow)),
                ('total_amount', models.IntegerField()),
                ('gst', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('due_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('products', models.ManyToManyField(related_name='inward_purchase_bill', to='prodinward.prodinward')),
            ],
        ),
    ]
