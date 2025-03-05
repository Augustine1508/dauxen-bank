from django.urls import path, include
from .views import HttpResponse, HomepageView, Login
from .signup import SignUp
from .login import Login, ProfileView
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .emailverify import Email_VerificationView




urlpatterns = [
    path('', HomepageView.as_view(), name='homeview'),
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('email_verify', Email_VerificationView.as_view(), name='email_verify'),
    path('profile', ProfileView.as_view(), name='profile'),
    
    path('accounts/', include('allauth.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

