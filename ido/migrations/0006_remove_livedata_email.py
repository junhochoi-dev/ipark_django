# Generated by Django 2.2.7 on 2021-07-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0005_livedata_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livedata',
            name='email',
        ),
    ]
