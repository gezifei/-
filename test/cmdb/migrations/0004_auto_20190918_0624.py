# Generated by Django 2.0.8 on 2019-09-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20190918_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('size', models.TextField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='idc',
            options={},
        ),
    ]
