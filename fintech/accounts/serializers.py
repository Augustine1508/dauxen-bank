from rest_framework import serializers
from .models import BankAccount, VirtualAccount, Transaction

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'user', 'account_number', 'balance', 'is_active', 'created_at']
        read_only_fields = ['account_number', 'balance', 'created_at']

class VirtualAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualAccount
        fields = '__all__'
        read_only_fields = ['account_number', 'created_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['reference', 'timestamp']
