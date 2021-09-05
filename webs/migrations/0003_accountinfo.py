# Generated by Django 3.2.7 on 2021-09-05 11:22

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0002_emailconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('means_of_id', models.CharField(blank=True, max_length=100, null=True)),
                ('mid_image', models.FileField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='media/identification'))),
                ('profile_image', models.FileField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='media/profile'))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account_info',
            },
        ),
    ]
