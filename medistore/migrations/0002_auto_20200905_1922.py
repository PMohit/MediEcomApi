# Generated by Django 3.0.7 on 2020-09-05 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medistore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='addresss',
            new_name='address',
        ),
    ]
