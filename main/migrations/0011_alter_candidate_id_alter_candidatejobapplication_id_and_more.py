# Generated by Django 4.2.3 on 2023-08-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_candidatejobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='candidatejobapplication',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='postjob',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
