# Generated by Django 3.0 on 2020-06-04 05:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_timemodel', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=200)),
                ('tz', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity_periods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api_demo_app.ActivityPeriod')),
            ],
        ),
    ]