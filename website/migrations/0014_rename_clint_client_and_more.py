# Generated by Django 4.1.4 on 2023-01-17 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_clint_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clint',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='Clintlogo',
            new_name='clientlogo',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='SolutionStandard',
            new_name='solutionstandard',
        ),
        migrations.RemoveField(
            model_name='homesetting',
            name='Clintnumber',
        ),
    ]