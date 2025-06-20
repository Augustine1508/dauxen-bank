from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.utils.timezone import now
from datetime import timedelta
import pyotp
import secrets
from django.db import models
from django.conf import settings
import uuid
# from django_otp.plugins.otp_totp.models import TOTPDevice


# Create your models here.
ACCOUNT_TYPE_CHOICES = [
    ('personal', 'personal'),
    ('business', 'business'),
]



class User(AbstractUser):
    id = ShortUUIDField(primary_key=True, unique=True, editable=False, alphabet='bcarem12345qop09867890')
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    account_type = models.CharField(
        max_length=10,
        choices=ACCOUNT_TYPE_CHOICES, default='personal'
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username


class PersonalAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='personalaccount')
    date_of_birth = models.DateField()
    image = models.ImageField( upload_to='profile')

    def __str__(self):
        return self.user.last_name


class BusinessAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='businessaccount')
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200)
    business_address = models.TextField()
    legal_name = models.CharField(max_length=255)
    logo = models.ImageField( upload_to='business_logos/', null=True, blank=True)

    def __str__(self):
        return self.user.last_name



class OTPCODE(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="otps")
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    phone_otp = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_otp_expired(self):
        if self.created_at is None:
            return True
        return now() > self.created_at + timedelta(minutes=10)

    def __str__(self):
        return self.user.email




class TwofactorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='twofactor')
    is_twofa_enabled = models.BooleanField(default=False)
    twofacode = models.CharField(max_length=200)
    twofactor_created = models.DateTimeField(blank=True, null=True)
    twofa_backup = models.JSONField(default=list, blank=True)
    is_email_enabled = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=200, blank=True, null=True)
    email_created = models.DateTimeField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    def generate_twofactor_secret(self):
        self.twofacode = pyotp.random_base32()
        self.save()


    def generate_twofactor_backup(self):
        self.twofa_backup = [secrets.token_hex(4) for _ in range(10)]
        self.save()


# here is model for account number



def generate_sequential_account_number():
    prefix = "305"
    last_account = BankAccount.objects.order_by('-id').first()
    next_seq = last_account.id + 1 if last_account else 1
    return f"{prefix}{str(next_seq).zfill(7)}"

class BankAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bank_account')
    account_number = models.CharField(max_length=10, unique=True, editable=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = generate_sequential_account_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} — {self.account_number}"

class VirtualAccount(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='virtual_accounts')
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=10, unique=True, editable=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = generate_sequential_account_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.account_number})"

class Transaction(models.Model):
    sender = models.ForeignKey(BankAccount, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(BankAccount, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=64, unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = uuid.uuid4().hex.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender.account_number} → {self.receiver.account_number} ({self.amount})"
