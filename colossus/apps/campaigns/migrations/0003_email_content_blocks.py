# Generated by Django 2.0.6 on 2018-06-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20180619_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='content_blocks',
            field=models.TextField(default='', verbose_name='blocks'),
            preserve_default=False,
        ),
    ]