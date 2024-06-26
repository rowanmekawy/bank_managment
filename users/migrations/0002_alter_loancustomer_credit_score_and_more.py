# Generated by Django 4.2.10 on 2024-03-24 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loancustomer',
            name='credit_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loanprovider',
            name='total_budget',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
