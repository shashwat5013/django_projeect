# Generated by Django 2.2.12 on 2020-05-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contest_details',
            fields=[
                ('registered_uesr_password', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('registered_uesr_webstie', models.CharField(max_length=20)),
                ('registered_uesr_image', models.ImageField(upload_to='media/Contest/')),
            ],
        ),
    ]
