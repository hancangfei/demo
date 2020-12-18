# Generated by Django 3.1.4 on 2020-12-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='adm_level',
            field=models.SmallIntegerField(choices=[(0, '区级'), (2, '市级'), (1, '县级'), (3, '省级'), (4, '最高检')], verbose_name='层级'),
        ),
        migrations.AlterField(
            model_name='procuratorate',
            name='org_level',
            field=models.SmallIntegerField(choices=[(0, '区级'), (2, '市级'), (1, '县级'), (3, '省级'), (4, '最高检')], verbose_name='检察院层级'),
        ),
    ]
