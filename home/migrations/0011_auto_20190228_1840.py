# Generated by Django 2.1.5 on 2019-02-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190226_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='empstatus',
            name='isPause',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empstatus',
            name='pauseTime',
            field=models.CharField(max_length=10, null=True),
        ),
    ]