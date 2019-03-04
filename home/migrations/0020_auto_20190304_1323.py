# Generated by Django 2.1.7 on 2019-03-04 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20190302_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='year',
            new_name='builtYear',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='cust_ID',
        ),
        migrations.RemoveField(
            model_name='product',
            name='features',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.AddField(
            model_name='complaints',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='sp', max_length=2),
        ),
    ]