# Generated by Django 3.1.2 on 2021-06-12 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information_system', '0004_deposits_member'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposits',
            options={'verbose_name_plural': 'Deposits'},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name_plural': 'Members'},
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_loan', models.DateTimeField(auto_now=True)),
                ('Amount_loan', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='information_system.members')),
            ],
            options={
                'verbose_name_plural': 'Loans',
            },
        ),
    ]
