from django.db import models
from category.models import Category


class Transaction(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type_transaction = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions_as_category')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.value)
