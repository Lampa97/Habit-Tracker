# Generated by Django 5.1.7 on 2025-03-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0003_alter_habit_owner_alter_habit_periodicity_in_days"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="last_scheduled",
            field=models.DateField(blank=True, null=True, verbose_name="Last scheduled"),
        ),
    ]
