# Generated by Django 5.1.3 on 2024-12-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_rename_location_locations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]
