# Generated by Django 4.0.3 on 2022-04-09 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='url',
            new_name='link',
        ),
    ]