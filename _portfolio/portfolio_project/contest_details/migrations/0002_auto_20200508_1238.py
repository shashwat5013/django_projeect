# Generated by Django 2.2.12 on 2020-05-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest_details',
            name='registered_uesr_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
