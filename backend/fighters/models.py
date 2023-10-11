from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Fighter(models.Model):
    name = models.CharField(max_length=255)
    race = models.ManyToManyField(Race)
    weapon = models.ManyToManyField(Weapon)
    strength = models.IntegerField(default=5)
    intelligence = models.IntegerField(default=5)
    agility = models.IntegerField(default=5)
    dexterity = models.IntegerField(default=5)
    endurance = models.IntegerField(default=5)

    def __str__(self):
        return self.name

