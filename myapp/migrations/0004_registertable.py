# Generated by Django 4.1.5 on 2023-01-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contacttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='registertable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Number', models.BigIntegerField()),
                ('Password', models.CharField(max_length=25)),
                ('Address', models.TextField()),
            ],
        ),
    ]
