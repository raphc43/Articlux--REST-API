# Generated by Django 2.2 on 2022-07-23 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleentry',
            name='topic',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleTopic'),
        ),
    ]
