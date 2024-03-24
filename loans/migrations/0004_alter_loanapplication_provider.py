# Generated by Django 4.2.10 on 2024-03-24 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_loancustomer_credit_score_and_more'),
        ('loans', '0003_loanapplication_remaining_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_provider', to='users.loanprovider'),
        ),
    ]