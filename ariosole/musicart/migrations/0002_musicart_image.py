# Generated by Django 4.1 on 2022-10-31 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicart',
            name='image',
            field=models.ImageField(default=1, upload_to='musicimage'),
            preserve_default=False,
        ),
    ]
