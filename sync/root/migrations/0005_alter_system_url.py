# Generated by Django 5.0.4 on 2024-04-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("root", "0004_alter_message_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="system",
            name="url",
            field=models.URLField(blank=True, null=True, verbose_name="URL"),
        ),
    ]
