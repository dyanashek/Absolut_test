# Generated by Django 5.0.4 on 2024-05-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('joined_project', models.DateTimeField(auto_now_add=True)),
                ('updated_info', models.DateTimeField(auto_now=True)),
                ('answers', models.JSONField(default='{}')),
            ],
        ),
    ]
