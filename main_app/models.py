from django.db import models
from datetime import date
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'), 
    ('D', 'Dinner'),
    ('S', 'Snacks')
)
class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length = 250)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length = 250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    food = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    #adding ref to main DOG model, delete all feeding orphans when dog is deleted.
    dog = models.ForeignKey(Dog, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.get_food_display()} on  {self.date}"

    class Meta: 
        ordering=['-date']

