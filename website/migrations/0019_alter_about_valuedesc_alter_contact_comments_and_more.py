# Generated by Django 4.1.4 on 2023-01-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_alter_features_shortdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='valuedesc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='comments',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='aboutdesc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='aboutmission',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='aboutvision',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='carrerdesc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='chooseusdesc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='logodesc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='signupdesc',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='storyaboutusdesc1',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='homesetting',
            name='storyaboutusdesc2',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='shortdesc',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='shortdesc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
