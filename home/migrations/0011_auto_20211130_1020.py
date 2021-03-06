# Generated by Django 3.2.6 on 2021-11-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211130_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couresalimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='hajj_posts',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='swalah_posts',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='swaum_posts',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='towhid_post',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='zakat_posts',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
