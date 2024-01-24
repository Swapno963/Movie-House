# Generated by Django 4.2.7 on 2024-01-24 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie_viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.IntegerField()),
                ('price', models.IntegerField()),
                ('realis_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='service/images/')),
                ('is_favourite', models.BooleanField()),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.moviesmodel')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_viewer.movieviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.moviesmodel')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_viewer.movieviewer')),
            ],
        ),
    ]