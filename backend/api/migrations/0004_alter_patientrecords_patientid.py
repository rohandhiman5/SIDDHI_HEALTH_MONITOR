# Generated by Django 5.0.6 on 2024-06-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_patientrecords_patientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecords',
            name='patientId',
            field=models.CharField(max_length=100),
        ),
    ]