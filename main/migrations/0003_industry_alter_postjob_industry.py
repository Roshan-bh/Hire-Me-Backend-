# Generated by Django 4.2.3 on 2023-08-11 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_postjob_industry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': '3. Industries',
            },
        ),
        migrations.AlterField(
            model_name='postjob',
            name='Industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.industry'),
        ),
    ]