# Generated by Django 5.1.4 on 2025-01-23 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('pages', models.CharField(max_length=100)),
                ('coin', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PodcastBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('time', models.CharField(max_length=100)),
                ('coin', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('time', models.CharField(max_length=100)),
                ('coin', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.language')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='lang.language')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='lang.level')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('audio', models.FileField(upload_to='audio/')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.language')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('audio_image', models.ImageField(upload_to='images/')),
                ('audio_name', models.CharField(max_length=100)),
                ('audio_description', models.TextField()),
                ('audio', models.FileField(upload_to='audio/')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='lang.level')),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('translation_flag', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('example', models.TextField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phrases', to='lang.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='images/')),
                ('video', models.FileField(upload_to='videos/')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.language')),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('translation_flag', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('example', models.TextField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabularies', to='lang.unit')),
            ],
        ),
    ]
