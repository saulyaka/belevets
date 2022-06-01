# Generated by Django 3.2.13 on 2022-05-10 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_public', models.TextField()),
                ('description_private', models.TextField(blank=True)),
                ('announcement', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('image', models.FileField(blank=True, upload_to='course/imges')),
                ('video', models.FileField(blank=True, upload_to='course/video')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.FileField(blank=True, upload_to='course/imges')),
                ('text', models.TextField(blank=True)),
                ('materials', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
                ('image', models.FileField(blank=True, upload_to='course/imges')),
                ('video', models.FileField(blank=True, upload_to='course/video')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section')),
            ],
        ),
    ]
