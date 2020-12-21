# Generated by Django 3.1.3 on 2020-11-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0016_auto_20201113_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_source', models.URLField(unique=True, verbose_name='Url (Source)')),
                ('url_watch', models.URLField(blank=True, default='', verbose_name='Url (Watch)')),
                ('url_thumbnail', models.URLField(blank=True, default='', verbose_name='Url (Thumbnail)')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.TextField(max_length=2048, verbose_name='Description')),
                ('duration', models.IntegerField(blank=True, default=0, verbose_name='Duration')),
                ('uploader_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Uploader name')),
                ('uploader_url', models.URLField(blank=True, default='', verbose_name='Uploader Url')),
            ],
            options={
                'verbose_name': 'Audio source',
                'verbose_name_plural': 'Audio sources',
            },
        ),
    ]
