# Generated by Django 4.2.6 on 2023-10-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('strength', models.IntegerField(default=5)),
                ('intelligence', models.IntegerField(default=5)),
                ('agility', models.IntegerField(default=5)),
                ('dexterity', models.IntegerField(default=5)),
                ('endurance', models.IntegerField(default=5)),
                ('race', models.ManyToManyField(to='fighters.race')),
                ('weapon', models.ManyToManyField(to='fighters.weapon')),
            ],
        ),
    ]