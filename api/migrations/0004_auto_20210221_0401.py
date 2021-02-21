# Generated by Django 3.1.7 on 2021-02-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210220_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='BPS',
            new_name='adhar',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='avatar',
            new_name='avatar1',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='DPS',
            new_name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='Gyroscope',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='vehicle_fuel',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='vehicle_pol',
        ),
        migrations.AddField(
            model_name='owner',
            name='avatar2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='owner',
            name='avatar3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='owner',
            name='avatar4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='owner',
            name='Address',
            field=models.CharField(max_length=100),
        ),
    ]
