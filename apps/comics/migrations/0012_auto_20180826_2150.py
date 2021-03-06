# Generated by Django 2.0.7 on 2018-08-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0011_comic_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='hr_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comic',
            name='font',
            field=models.FileField(blank=True, default='', upload_to=''),
            preserve_default=False,
        ),
    ]
