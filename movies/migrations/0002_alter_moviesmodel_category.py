# Generated by Django 4.2.7 on 2024-01-24 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.categorymodel'),
        ),
    ]