# Generated by Django 3.1.2 on 2020-10-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
