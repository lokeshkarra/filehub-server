# Generated by Django 4.2.9 on 2025-03-28 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='user_files/', validators=[files.models.validate_file_type])),
                ('filename', models.CharField(max_length=255)),
                ('size', models.BigIntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
