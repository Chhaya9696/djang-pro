# Generated by Django 5.0 on 2024-03-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
