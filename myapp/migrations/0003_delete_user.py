# Generated by Django 5.0.4 on 2024-04-24 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_student_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
