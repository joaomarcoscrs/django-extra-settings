# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extra_settings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="setting",
            name="value_duration",
            field=models.DurationField(blank=True, null=True, verbose_name="Value"),
        ),
        migrations.AlterField(
            model_name="setting",
            name="value_type",
            field=models.CharField(
                choices=[
                    ("bool", "bool"),
                    ("date", "date"),
                    ("datetime", "datetime"),
                    ("decimal", "decimal"),
                    ("duration", "duration"),
                    ("email", "email"),
                    ("file", "file"),
                    ("float", "float"),
                    ("image", "image"),
                    ("int", "int"),
                    ("string", "string"),
                    ("text", "text"),
                    ("time", "time"),
                    ("url", "url"),
                ],
                max_length=20,
                verbose_name="Type",
            ),
        ),
    ]
