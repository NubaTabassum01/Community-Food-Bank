from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=100)
    member_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class FoodStock(models.Model):
    quantity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.quantity} units available"


class Distribution(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.family.name} - {self.quantity}"