# Generated by Django 4.0.6 on 2022-07-20 04:59

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='videos/', validators=[api.validators.validate_file_type, api.validators.validate_size])),
                ('uploaded_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
