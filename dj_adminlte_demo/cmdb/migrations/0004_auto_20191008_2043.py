# Generated by Django 2.0.8 on 2019-10-08 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20191008_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='size',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='U型的大小'),
        ),
    ]
