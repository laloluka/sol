# Generated by Django 3.1.2 on 2021-06-11 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information_system', '0003_deposits'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposits',
            name='Member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='information_system.members'),
        ),
    ]