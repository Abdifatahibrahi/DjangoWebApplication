# Generated by Django 3.2.6 on 2021-11-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
