# Generated by Django 3.1.7 on 2021-02-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_auto_20210221_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrecord',
            name='status',
            field=models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=11),
        ),
    ]
