# Generated by Django 3.2.4 on 2021-06-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0002_alter_covidrecord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidrecord',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
