# Generated by Django 5.1.1 on 2024-09-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('category', models.CharField(choices=[('psychometric', 'Psychometric'), ('aptitude', 'Aptitude'), ('reasoning', 'Reasoning')], max_length=50)),
                ('subcategory', models.CharField(choices=[('o_score', 'O Score'), ('c_score', 'C Score'), ('e_score', 'E Score'), ('a_score', 'A Score'), ('n_score', 'N Score'), ('numerical', 'Numerical'), ('spatial', 'Spatial'), ('perceptual', 'Perceptual'), ('verbal', 'Verbal'), ('logical', 'Logical')], max_length=50)),
                ('option_1', models.CharField(max_length=255)),
                ('option_2', models.CharField(max_length=255)),
                ('option_3', models.CharField(max_length=255)),
                ('option_4', models.CharField(max_length=255)),
                ('correct_option', models.CharField(max_length=255)),
                ('option_1_score', models.IntegerField(default=0)),
                ('option_2_score', models.IntegerField(default=0)),
                ('option_3_score', models.IntegerField(default=0)),
                ('option_4_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='logical',
            new_name='logical_reasoning',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='numerical',
            new_name='numerical_ability',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='perceptual',
            new_name='perceptual_ability',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='spatial',
            new_name='spatial_ability',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='verbal',
            new_name='verbal_reasoning',
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
    ]
