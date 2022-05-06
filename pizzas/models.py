from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'toppings'
    def __str__ (self):
        return f"{self.topping_name[:50]}..."


class Reviews(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    reviews = models.TextField()
    def __str__ (self):
        return f"{self.comments[:50]}..."
        