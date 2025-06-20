from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BankAccount, Transaction

@login_required
def dashboard_view(request):
    try:
        account = BankAccount.objects.get(user=request.user)
        transactions = Transaction.objects.filter(
            sender=account
        ) | Transaction.objects.filter(
            receiver=account
        )
    except BankAccount.DoesNotExist:
        account = None
        transactions = []

    return render(request, 'dashboard.html', {
        'account': account,
        'transactions': transactions,
    })
