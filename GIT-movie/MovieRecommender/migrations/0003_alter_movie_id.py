# Generated by Django 4.2.7 on 2024-03-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRecommender', '0002_alter_movie_image_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
