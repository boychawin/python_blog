# Generated by Django 3.2.5 on 2021-07-31 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactmessage_reply_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='reply_to',
            new_name='reply',
        ),
    ]