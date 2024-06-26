# Generated by Django 5.0.2 on 2024-02-26 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowhub", "0003_alter_comment_options_alter_articles_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articles",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories_articles",
                to="knowhub.category",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.TextField(max_length=300),
        ),
    ]
