# Generated by Django 3.1.7 on 2021-02-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crop',
            fields=[
                ('crop_id', models.AutoField(primary_key=True, serialize=False)),
                ('cropName', models.CharField(max_length=30)),
                ('cropType', models.CharField(max_length=10)),
                ('totalStorage', models.IntegerField(default=0)),
                ('cropSeason', models.CharField(max_length=10)),
            ],
        ),
    ]