from django.db import models


# Expense Model
class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.amount}'

# Income Model
class Income(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    comment = models.TextField()  

    def __str__(self):
        return f'{self.name}, {self.amount}'  
# Other Finacial Model
class OtherFinancials(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    comment = models.TextField()  

    def __str__(self):
        return f'{self.name}, {self.amount}'  
