# Generated by Django 5.0.6 on 2024-06-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
    ]
