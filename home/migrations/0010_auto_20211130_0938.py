# Generated by Django 3.2.6 on 2021-11-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211127_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='hajj_posts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='swalah_posts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='swaum_posts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='towhid_post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zakat_posts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]