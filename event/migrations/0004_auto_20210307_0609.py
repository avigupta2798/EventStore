# Generated by Django 3.1.7 on 2021-03-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20210306_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]