# Generated by Django 4.2.14 on 2024-07-16 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_remove_employee_farm_remove_farm_horses_horse_farm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='farm',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='farm.farm'),
        ),
    ]