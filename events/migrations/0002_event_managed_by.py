# Generated by Django 3.1 on 2021-05-01 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hosts', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='managed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosts.volunteer'),
        ),
    ]
