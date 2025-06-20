# import qrcode
# import io
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django_otp.plugins.otp_totp.models import TOTPDevice

# @login_required
# def generate_qr_code(request):
#     user = request.user
#     device, created = TOTPDevice.objects.get_or_create(user=user, name="Google Authenticator")
    
#     if not device.confirmed:  # Only generate a new QR code if not confirmed
#         otp_uri = device.config_url
#         qr = qrcode.make(otp_uri)
#         buffer = io.BytesIO()
#         qr.save(buffer, format="PNG")
#         return HttpResponse(buffer.getvalue(), content_type="image/png")

#     return HttpResponse("2FA Already Enabled", status=400)

# @login_required
# def enable_2fa(request):
#     user = request.user
#     if request.method == "POST":
#         token = request.POST.get("token")
#         device = TOTPDevice.objects.filter(user=user, name="Google Authenticator").first()

#         if device and device.verify_token(token):
#             device.confirmed = True
#             device.save()
#             return redirect("profile")  # Redirect to a success page
#         else:
#             return render(request, "enable_2fa.html", {"error": "Invalid code. Try again!"})

#     return render(request, "enable_2fa.html")



