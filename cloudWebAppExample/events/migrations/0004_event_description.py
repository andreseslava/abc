# Generated by Django 3.0.2 on 2020-01-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200127_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]