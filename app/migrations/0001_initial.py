# Generated by Django 4.2.4 on 2023-10-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('sage', models.IntegerField()),
                ('smail', models.EmailField(max_length=254)),
            ],
        ),
    ]
