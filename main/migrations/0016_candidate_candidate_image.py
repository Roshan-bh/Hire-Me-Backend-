# Generated by Django 4.2.3 on 2023-08-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_candidate_confirm_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='candidate_image',
            field=models.ImageField(null=True, upload_to='images/candidate_images/'),
        ),
    ]