# Generated by Django 3.2.13 on 2022-05-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleinair', '0003_rename_upload_image_pleinair_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pleinair',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
