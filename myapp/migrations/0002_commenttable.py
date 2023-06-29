# Generated by Django 4.1.5 on 2023-01-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='commenttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Website', models.CharField(max_length=20)),
                ('Message', models.TextField()),
            ],
        ),
    ]
