# Generated by Django 5.0.2 on 2024-02-16 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("knowhub", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ("creation",)},
        ),
    ]
