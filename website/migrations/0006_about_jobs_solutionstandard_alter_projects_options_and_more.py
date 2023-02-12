# Generated by Django 4.1.4 on 2023-01-03 04:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_homesetting_logodesc'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuename', models.CharField(blank=True, max_length=20, null=True)),
                ('valuedesc', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(blank=True, max_length=100, null=True)),
                ('shortdesc', models.CharField(blank=True, max_length=100, null=True)),
                ('jobdesc', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Add Jobs',
                'verbose_name_plural': 'Add Jobs',
            },
        ),
        migrations.CreateModel(
            name='SolutionStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ordering', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Solution Standard',
                'verbose_name_plural': 'Solution Standard',
            },
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Solution Catagory', 'verbose_name_plural': 'Solution Catagory'},
        ),
        migrations.AddField(
            model_name='homesetting',
            name='aboutbanner1',
            field=models.ImageField(blank=True, null=True, upload_to='static/modules/'),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='aboutbanner2',
            field=models.ImageField(blank=True, null=True, upload_to='static/modules/'),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='aboutdesc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='aboutmission',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='abouttitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='aboutvision',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='carrerbanner',
            field=models.ImageField(blank=True, null=True, upload_to='static/modules/'),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='carrerdesc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='carrerjobtitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homesetting',
            name='carrertitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='SolutionStandard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Projects', to='website.solutionstandard'),
            preserve_default=False,
        ),
    ]
