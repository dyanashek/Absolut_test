# Generated by Django 5.0.4 on 2024-05-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_question_type_alter_quiz_label_alter_quiz_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('MultipleChoice', 'Выбор нескольких вариантов'), ('Choice', 'Выбор одного варианта')], max_length=15),
        ),
    ]
