# Generated by Django 4.0 on 2023-01-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('en_title', models.CharField(max_length=255)),
                ('en_body', models.TextField()),
                ('de_title', models.CharField(max_length=255)),
                ('de_body', models.TextField()),
                ('fr_title', models.CharField(max_length=255)),
                ('fr_body', models.TextField()),
            ],
        ),
    ]
