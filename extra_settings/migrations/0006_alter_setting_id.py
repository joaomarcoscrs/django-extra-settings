# Generated by Django 4.0.4 on 2022-06-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extra_settings", "0005_setting_value_json_alter_setting_value_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="setting",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
