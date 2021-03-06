# Generated by Django 3.1.4 on 2020-12-18 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
        ('wenshu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docplan',
            name='plan_case',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='cases.case', verbose_name='文书所属案件'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docreport',
            name='rep_case',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='cases.case', verbose_name='文书所属案件'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docsuggestion',
            name='sug_case',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sugs', to='cases.case', verbose_name='文书所属案件'),
            preserve_default=False,
        ),
    ]
