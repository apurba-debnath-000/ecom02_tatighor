# Generated by Django 3.2.7 on 2022-09-18 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store', '0005_alter_userprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='krishok',
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(default=1, limit_choices_to={'groups__name': 'Manufacturer'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(default='piece', on_delete=django.db.models.deletion.CASCADE, to='Store.unit_type'),
        ),
    ]
