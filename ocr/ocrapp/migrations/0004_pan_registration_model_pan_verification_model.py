# Generated by Django 2.1.7 on 2019-04-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0003_auto_20190402_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='pan_registration_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_num', models.CharField(max_length=50, unique=True)),
                ('dob', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='pan_verification_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_num', models.CharField(max_length=50, unique=True)),
                ('dob', models.CharField(max_length=11)),
            ],
        ),
    ]