# Generated by Django 3.2.5 on 2021-12-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ackley', '0002_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(height_field=225, upload_to='static\\images', width_field=294)),
                ('Img_name', models.CharField(max_length=20)),
                ('Img_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='bookings',
            name='No_of_days',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='No_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Phone_number',
            field=models.CharField(default='not given', max_length=10),
        ),
    ]