# Generated by Django 2.1.7 on 2019-04-02 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0002_aadhar_registration_model_aadhar_verification_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aadhar_registration_model',
            name='address',
        ),
        migrations.RemoveField(
            model_name='aadhar_verification_model',
            name='address',
        ),
    ]
