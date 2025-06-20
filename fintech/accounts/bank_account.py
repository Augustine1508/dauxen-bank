from rest_framework import viewsets, permissions
from .models import BankAccount, VirtualAccount, Transaction
from .serializers import BankAccountSerializer, VirtualAccountSerializer, TransactionSerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()  # ✅ REQUIRED
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BankAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VirtualAccountViewSet(viewsets.ModelViewSet):
    queryset = VirtualAccount.objects.all()  # ✅ REQUIRED
    serializer_class = VirtualAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VirtualAccount.objects.filter(bank_account__user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()  # ✅ REQUIRED
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(
            sender__user=self.request.user
        ) | Transaction.objects.filter(
            receiver__user=self.request.user
        )
