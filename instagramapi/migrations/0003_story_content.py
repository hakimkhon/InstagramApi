# Generated by Django 4.0.5 on 2022-06-22 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapi', '0002_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]