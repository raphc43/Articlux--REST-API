# Generated by Django 2.2 on 2022-07-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20220723_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletopic',
            name='text',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]