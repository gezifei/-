# Generated by Django 2.0.8 on 2019-09-29 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_auto_20190919_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='idc_num',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='IDC_RACK', to='cmdb.Idc'),
        ),
    ]
