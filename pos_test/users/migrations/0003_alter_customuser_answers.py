# Generated by Django 5.0.4 on 2024-05-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='answers',
            field=models.JSONField(default=dict),
        ),
    ]
