# Generated by Django 2.1.5 on 2019-02-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190226_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empstatus',
            name='loginTime',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='empstatus',
            name='logoutTime',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
