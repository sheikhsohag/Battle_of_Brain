# Generated by Django 4.2.4 on 2023-10-01 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('quizs', '0008_question_question_slug_alter_question_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='choise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.category')),
            ],
        ),
    ]
