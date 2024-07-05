# Generated by Django 4.2.5 on 2024-07-04 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options_alter_driver_options_and_more'),
        ('trips', '0003_alter_car_car_status_alter_car_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='driver',
        ),
        migrations.AddField(
            model_name='rating',
            name='passenger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rating_left', to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_received', to='users.driver'),
        ),
    ]
