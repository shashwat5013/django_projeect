# Generated by Django 2.2.12 on 2020-05-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_user_password', models.CharField(max_length=20)),
                ('registered_user_project_name', models.CharField(max_length=20)),
                ('registered_user_project_details', models.TextField()),
            ],
        ),
    ]
