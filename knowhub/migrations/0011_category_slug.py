# Generated by Django 5.0.2 on 2024-03-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowhub", "0010_services_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
