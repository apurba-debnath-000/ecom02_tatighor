# Generated by Django 3.2.7 on 2021-10-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]