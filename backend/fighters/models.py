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
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, blank=True, null=True, on_delete=models.CASCADE)
    strength = models.IntegerField(default=5)
    intelligence = models.IntegerField(default=5)
    agility = models.IntegerField(default=5)
    dexterity = models.IntegerField(default=5)
    endurance = models.IntegerField(default=5)
    image = models.ImageField(upload_to="static/images/fighters/", blank=True, null=True)
    def __str__(self):
        return self.name
