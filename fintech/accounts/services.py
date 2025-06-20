from django.db import transaction
from django.core.exceptions import ValidationError
from .models import BankAccount, Transaction

def transfer_funds(sender: BankAccount, receiver: BankAccount, amount: float):
    if amount <= 0:
        raise ValidationError("Amount must be positive.")
    if sender.balance < amount:
        raise ValidationError("Insufficient funds.")

    with transaction.atomic():
        sender.balance -= amount
        receiver.balance += amount
        sender.save()
        receiver.save()

        Transaction.objects.create(
            sender=sender,
            receiver=receiver,
            amount=amount
        )
