# Generated by Django 5.0 on 2024-03-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
