# Generated by Django 3.0.3 on 2020-02-14 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeageTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leage_type', models.CharField(max_length=100)),
                ('my_deck_name', models.CharField(max_length=100)),
                ('record', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]