# Generated by Django 4.2.7 on 2023-12-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]