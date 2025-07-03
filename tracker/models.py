from django.db import models

# Create your models here.


class CurrentBalance(models.Model):
    current_balance=models.FloatField(default=0)

    def __str__(self):
        return f"balance is {self.current_balance}"
    

class TrackingHistory(models.Model):
    current_balance=models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    amount=models.FloatField()
    expense_type=models.CharField(max_length=50,choices=(('credit','credit'),('debit','debit')))
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The amount is {self.amount} for {self.description} , The expense is {self.expense_type} type"
    

class RequestLogs(models.Model):
    request_info=models.TextField()
    request_path=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    request_method=models.CharField(max_length=100)

