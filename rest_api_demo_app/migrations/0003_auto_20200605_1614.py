# Generated by Django 3.0 on 2020-06-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_demo_app', '0002_auto_20200604_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activity_periods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_api_demo_app.ActivityPeriod'),
        ),
    ]
