# Generated by Django 5.0.4 on 2024-05-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_alter_question_type_alter_quiz_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='type',
            field=models.CharField(choices=[('MultipleChoice', 'Выбор нескольких вариантов'), ('Choice', 'Выбор одного варианта')], max_length=1500),
        ),
    ]