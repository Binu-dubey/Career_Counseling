# Generated by Django 5.1.1 on 2024-09-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assessment", "0003_remove_userprofile_perceptual_ability_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="category",
            field=models.CharField(
                choices=[
                    ("psychometric", "Psychometric"),
                    ("aptitude", "Aptitude"),
                    ("reasoning", "Reasoning"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="subcategory",
            field=models.CharField(
                choices=[
                    ("o_score", "O Score"),
                    ("c_score", "C Score"),
                    ("e_score", "E Score"),
                    ("a_score", "A Score"),
                    ("n_score", "N Score"),
                    ("numerical", "Numerical"),
                    ("verbal", "Verbal"),
                    ("logical", "Logical"),
                ],
                max_length=255,
            ),
        ),
    ]
