from django.urls import path, include
from .views import HttpResponse, HomepageView, Login
from .signup import SignUp
from .login import Login
from .profile import  ProfileView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .emailverify import Email_VerificationView
from .two_fasetup import Setup2Fa
from rest_framework.routers import DefaultRouter
from .bank_account import BankAccountViewSet, VirtualAccountViewSet, TransactionViewSet
from .dashboard import dashboard_view


router = DefaultRouter()
router.register(r'bank-accounts', BankAccountViewSet)
router.register(r'virtual-accounts', VirtualAccountViewSet)
router.register(r'transactions', TransactionViewSet)



urlpatterns = [
    path('', HomepageView.as_view(), name='homeview'),
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('email_verify', Email_VerificationView.as_view(), name='email_verify'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('twofa', Setup2Fa.as_view(), name='twofa'),
    # path('twofaverify', Verify2fatoken.as_view(), name='twofaverify'),
    
    path('accounts/', include('allauth.urls')),
    path('google-login/', lambda request: redirect('/accounts/google/login/')),
    path('api/', include(router.urls)),
    path('dashboard/', dashboard_view, name='dashboard'),

    
    
    

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

