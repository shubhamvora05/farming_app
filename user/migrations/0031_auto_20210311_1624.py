# Generated by Django 3.1.7 on 2021-03-11 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_userrecord_crop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrecord',
            old_name='crop',
            new_name='selectCrop',
        ),
    ]