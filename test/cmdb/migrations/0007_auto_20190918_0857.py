# Generated by Django 2.0.8 on 2019-09-18 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20190918_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='idc_num',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.Idc'),
        ),
    ]
