# Generated by Django 4.1.4 on 2023-01-15 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_events_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carspecs',
            old_name='car_brand',
            new_name='car_make',
        ),
        migrations.AddField(
            model_name='carplan',
            name='car_specs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='car_events_api.carspecs'),
        ),
        migrations.AlterField(
            model_name='carspecs',
            name='production_year',
            field=models.IntegerField(),
        ),
    ]
