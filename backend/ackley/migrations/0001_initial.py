# Generated by Django 3.2.5 on 2021-11-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=10)),
                ('Message', models.TextField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]