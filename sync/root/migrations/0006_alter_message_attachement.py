# Generated by Django 5.0.4 on 2024-04-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("root", "0005_alter_system_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="attachement",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="attachments",
                verbose_name="attachement",
            ),
        ),
    ]
