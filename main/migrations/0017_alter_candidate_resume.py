# Generated by Django 4.2.3 on 2023-08-17 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_candidate_candidate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]