# Generated by Django 4.0.1 on 2023-04-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('article', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Bangladeshi English Newspaper',
            },
        ),
    ]