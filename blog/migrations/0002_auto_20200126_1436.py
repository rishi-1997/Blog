# Generated by Django 2.2.6 on 2020-01-26 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='update',
            new_name='updated',
        ),
    ]
