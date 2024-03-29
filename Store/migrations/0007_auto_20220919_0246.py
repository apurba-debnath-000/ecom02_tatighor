# Generated by Django 3.2.7 on 2022-09-18 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_auto_20220919_0227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='manufacturer',
            new_name='Manufacturer',
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(default='kg', on_delete=django.db.models.deletion.CASCADE, to='Store.unit_type'),
        ),
    ]
