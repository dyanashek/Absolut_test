# Generated by Django 5.0.4 on 2024-05-04 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_rename_answers_questionnairequestion_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnairequiz',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='questionnairequiz',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='questionnairequiz',
            name='user',
        ),
        migrations.DeleteModel(
            name='QuestionnaireQuestion',
        ),
        migrations.DeleteModel(
            name='QuestionnaireQuiz',
        ),
    ]
