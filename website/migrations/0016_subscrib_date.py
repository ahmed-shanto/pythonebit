# Generated by Django 4.1.4 on 2023-01-17 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_about_ordering_about_status_jobs_ordering_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscrib',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
