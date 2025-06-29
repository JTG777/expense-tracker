from django.db import models

# Create your models here.


class CurrentBalance(models.Model):
    current_balance=models.FloatField(default=0)
    

class TrackingHistory(models.Model):
    current_balance=models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    amount=models.FloatField()
    expense_type=models.CharField(max_length=50,choices=(('credit','credit'),('debit','debit')))
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

