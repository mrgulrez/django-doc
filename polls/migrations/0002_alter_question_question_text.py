# Generated by Django 4.1.6 on 2023-07-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='write your question here', max_length=200),
        ),
    ]