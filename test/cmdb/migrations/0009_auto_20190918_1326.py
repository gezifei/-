# Generated by Django 2.0.8 on 2019-09-18 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmdb', '0008_auto_20190918_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='user',
            field=models.ManyToManyField(default='', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rack',
            name='idc_num',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='IDC_RACK', to='cmdb.Idc'),
        ),
    ]
