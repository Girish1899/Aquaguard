# Generated by Django 2.1.5 on 2019-03-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20190303_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
