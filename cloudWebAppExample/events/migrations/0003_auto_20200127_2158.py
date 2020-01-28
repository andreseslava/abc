# Generated by Django 3.0.2 on 2020-01-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200121_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='endDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='mode',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='startDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default='new Event', max_length=180),
        ),
    ]