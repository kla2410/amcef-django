# Generated by Django 5.0.6 on 2024-06-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_content',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
    ]
