# Generated by Django 2.1.5 on 2019-02-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190226_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profilePicture',
            field=models.ImageField(null=True, upload_to='home/static/images/employee/'),
        ),
    ]
