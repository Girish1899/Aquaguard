# Generated by Django 2.1.7 on 2019-03-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190302_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='severity',
            field=models.IntegerField(default=1, max_length=5),
        ),
    ]
