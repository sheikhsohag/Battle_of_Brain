# Generated by Django 4.2.4 on 2023-09-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizs', '0002_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]
