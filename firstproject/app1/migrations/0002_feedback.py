# Generated by Django 5.0 on 2024-02-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
