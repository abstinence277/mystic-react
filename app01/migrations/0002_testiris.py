# Generated by Django 3.2 on 2023-04-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestIris',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sepallength', models.FloatField()),
                ('sepalwidth', models.FloatField()),
                ('label', models.IntegerField(default=1)),
            ],
        ),
    ]