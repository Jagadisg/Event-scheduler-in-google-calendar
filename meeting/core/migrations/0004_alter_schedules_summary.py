# Generated by Django 4.2.10 on 2024-08-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_schedules_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='summary',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
