# Generated by Django 5.0.6 on 2024-06-15 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_api', '0002_user_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_content',
            old_name='userid',
            new_name='userId',
        ),
        migrations.RenameField(
            model_name='user_details',
            old_name='userid',
            new_name='userId',
        ),
    ]
