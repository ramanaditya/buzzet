# Generated by Django 2.1.7 on 2019-04-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0010_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='name',
            field=models.CharField(default='enter username', max_length=50),
        ),
        migrations.AddField(
            model_name='community',
            name='rating',
            field=models.FloatField(blank=True, default=2, null=True),
        ),
    ]