# Generated by Django 5.0.3 on 2024-03-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MovieRecommender", "0004_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="trailerlink",
            field=models.CharField(default=545, max_length=250),
            preserve_default=False,
        ),
    ]