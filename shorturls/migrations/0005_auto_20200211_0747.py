# Generated by Django 3.0.3 on 2020-02-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturls', '0004_auto_20200211_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_urls',
            name='short_url',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]