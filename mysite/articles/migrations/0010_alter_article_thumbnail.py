# Generated by Django 5.1.5 on 2025-04-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default='../images/default.jpg', upload_to='images/'),
        ),
    ]
