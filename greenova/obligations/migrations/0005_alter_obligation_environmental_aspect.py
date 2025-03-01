# Generated by Django 5.1.6 on 2025-02-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("obligations", "0004_alter_obligation_project_phase"),
    ]

    operations = [
        migrations.AlterField(
            model_name="obligation",
            name="environmental_aspect",
            field=models.CharField(
                choices=[
                    ("Air", "Air"),
                    ("Water", "Water"),
                    ("Waste", "Waste"),
                    ("Energy", "Energy"),
                    ("Biodiversity", "Biodiversity"),
                    ("Noise", "Noise"),
                    ("Chemicals", "Chemicals"),
                    ("Soil", "Soil"),
                    ("Other", "Other"),
                ],
                max_length=255,
            ),
        ),
    ]
