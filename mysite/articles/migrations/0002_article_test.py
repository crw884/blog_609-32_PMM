# Generated by Django 5.1.5 on 2025-03-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
