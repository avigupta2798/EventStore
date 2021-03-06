# Generated by Django 3.1.7 on 2021-03-06 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/')),
                ('title', models.CharField(max_length=250, null=True)),
                ('content_text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('is_liked', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
