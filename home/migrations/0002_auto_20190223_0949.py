# Generated by Django 2.1.5 on 2019-02-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='leads',
            name='isContacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='leads',
            name='isInterested',
            field=models.BooleanField(default=False),
        ),
    ]
