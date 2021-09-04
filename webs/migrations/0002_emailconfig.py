# Generated by Django 3.2.7 on 2021-09-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='email', max_length=10)),
                ('port', models.BigIntegerField(blank=True, null=True)),
                ('is_tls', models.BooleanField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('host', models.CharField(blank=True, max_length=100, null=True)),
                ('default_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'email_config',
            },
        ),
    ]