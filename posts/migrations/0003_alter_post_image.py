# Generated by Django 5.1 on 2024-08-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_ezt2rj', upload_to='images/'),
        ),
    ]
