from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = "transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])

    def __str__(self):
        return f"{self.category} - {self.amount}"
