# Generated by Django 4.0.4 on 2022-07-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_profile_firma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='firma',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
