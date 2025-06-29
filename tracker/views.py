from django.shortcuts import render,redirect
from .models import TrackingHistory,CurrentBalance

# Create your views here.
def index(request):
    if request.method=='POST':
        current_balance,created=CurrentBalance.objects.get_or_create(id=1)
        amount=request.POST.get('amount')
        description=request.POST.get('description')

        expense_type='credit' if float(amount)>0 else 'debit'
        
        tracking_history=TrackingHistory.objects.create(amount=amount,description=description,expense_type=expense_type,current_balance=current_balance)
        current_balance.current_balance+=float(tracking_history.amount)
        current_balance.save()
        return redirect('index')
    
    current_balance,created=CurrentBalance.objects.get_or_create(id=1)

    income=0
    expense=0

    for transaction in TrackingHistory.objects.all():
        if transaction.expense_type=='credit':
            income+=transaction.amount
        else:
            expense+=transaction.amount

    context={
        'income':income,
        'expense':expense,
        'transactions':TrackingHistory.objects.all(),
        'current_balance':current_balance
    }


    
    return render(request,'index.html',context)

def remove_transaction(request,pk):
    transaction=TrackingHistory.objects.get(id=pk)
    current_balance=CurrentBalance.objects.get(id=1)
    current_balance.current_balance-=transaction.amount
    current_balance.save()
    transaction.delete()
    
    return redirect('index')