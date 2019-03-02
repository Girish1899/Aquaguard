# Generated by Django 2.1.5 on 2019-03-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_employee_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profilePicture',
            field=models.ImageField(null=True, upload_to='home/static/images/employee/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_logo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]