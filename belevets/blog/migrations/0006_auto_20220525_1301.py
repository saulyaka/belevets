# Generated by Django 3.2.13 on 2022-05-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_username_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='extra_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
