# Generated by Django 4.2.6 on 2023-10-11 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0002_remove_fighter_race_fighter_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fighters.race'),
        ),
    ]
