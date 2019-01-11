# Generated by Django 2.1.4 on 2019-01-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=196)),
                ('message', models.TextField()),
            ],
        ),
    ]