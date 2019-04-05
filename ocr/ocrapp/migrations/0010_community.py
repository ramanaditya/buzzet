# Generated by Django 2.1.7 on 2019-04-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0009_remove_photo_im_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=10000)),
                ('purpose', models.CharField(max_length=100)),
                ('descr', models.CharField(max_length=2000)),
                ('exp_profit', models.IntegerField(default=1)),
            ],
        ),
    ]