# Generated by Django 3.2.13 on 2022-05-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('users', '0004_rename_plein_air_userprofile_pleinair'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='comments',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
