# Generated by Django 5.0.6 on 2024-07-02 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created_by',
        ),
    ]
