# Generated by Django 3.2.7 on 2021-09-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0003_accountinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfo',
            name='user_no',
            field=models.TextField(blank=True, null=True),
        ),
    ]
