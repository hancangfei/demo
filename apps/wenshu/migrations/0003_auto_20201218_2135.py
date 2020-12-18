# Generated by Django 3.1.4 on 2020-12-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wenshu', '0002_auto_20201218_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='docplan',
            name='plan_title',
            field=models.CharField(default=None, max_length=128, verbose_name='文书标题'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docplan',
            name='plan_id',
            field=models.CharField(max_length=64, verbose_name='文书号'),
        ),
    ]
