# Generated by Django 2.2.12 on 2020-05-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='REGISTERED_USER_DETAIL',
            fields=[
                ('registered_uesr_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('registered_uesr_password', models.CharField(max_length=50)),
            ],
        ),
    ]