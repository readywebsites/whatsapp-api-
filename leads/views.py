import secrets
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Lead
from .serializers import LeadSerializer


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def webhook(request):
    expected = getattr(settings, "DRF_WEBHOOK_TOKEN", "").strip()

    # Handle Meta (WhatsApp / Facebook) Webhook Verification (GET request)
    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and challenge:
            if not expected or (token and secrets.compare_digest(token, expected)):
                return HttpResponse(challenge, content_type="text/plain", status=status.HTTP_200_OK)
            return Response(
                {"error": "Verification token mismatch"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response(
            {"error": "Invalid verification request"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Handle Webhook Payload (POST request)
    if expected:
        auth = request.headers.get("Authorization", "")
        supplied = auth[7:].strip() if auth.lower().startswith("bearer ") else ""
        if not supplied or not secrets.compare_digest(supplied, expected):
            return Response(
                {"success": False, "error": "Invalid webhook token"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
        lead = serializer.save()
        return Response(
            {"success": True, "message": "Lead received", "lead_id": lead.id},
            status=status.HTTP_201_CREATED,
        )

    return Response(
        {"success": False, "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )

