# Generated by Django 3.1.6 on 2021-02-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210212_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecord',
            name='farmImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
