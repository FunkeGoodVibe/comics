# Generated by Django 2.1.1 on 2018-10-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0019_remove_tag_comic'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagtype',
            name='default_icon',
            field=models.ImageField(blank=True, help_text='Tags without an image will use this instead.', upload_to=''),
        ),
    ]