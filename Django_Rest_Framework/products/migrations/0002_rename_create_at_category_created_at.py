# Generated by Django 5.0.6 on 2024-06-03 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
