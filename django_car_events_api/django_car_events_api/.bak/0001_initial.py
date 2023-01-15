# Generated by Django 4.1.4 on 2023-01-14 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('event_name', models.CharField(max_length=32)),
                ('event_location', models.CharField(max_length=60)),
                ('topic', models.CharField(max_length=60)),
                ('post', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='CarPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=20)),
                ('year_of_warranty', models.PositiveBigIntegerField(default=1)),
                ('finance_plan', models.CharField(
                    default='unavailable', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('production_year', models.CharField(max_length=20)),
                ('car_brand', models.CharField(max_length=60)),
                ('car_model', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=50)),
                ('image_link', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=60)),
                ('item_name', models.CharField(max_length=60)),
                ('item_description', models.CharField(max_length=200)),
                ('item_price', models.CharField(max_length=20)),
                ('image_link', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]