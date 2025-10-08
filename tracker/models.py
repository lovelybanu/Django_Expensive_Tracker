from django.db import models

# Create your models here.
class CurrentBalance(models.Model):
    current_balance=models.FloatField(default=0.0)

class TrackingHistory(models.Model):
    current_balance=models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    amount=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    expense_type=models.CharField(choices=(('CREDIT','CREDIT'),('DEBIT','DEBIT')),max_length=10)