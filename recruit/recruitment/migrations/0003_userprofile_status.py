# Generated by Django 2.0.6 on 2018-06-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20180609_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
