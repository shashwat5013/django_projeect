# Generated by Django 2.2.12 on 2020-05-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200509_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_user_detail',
            name='registered_uesr_accomplishment',
            field=models.CharField(default='No enteries made', max_length=400),
        ),
    ]