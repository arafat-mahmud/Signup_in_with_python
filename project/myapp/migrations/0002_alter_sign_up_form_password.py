# Generated by Django 5.1.3 on 2024-11-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up_form',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
