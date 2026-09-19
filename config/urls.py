from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({
        "success": True,
        "message": "Biz499 Lead API is running",
        "webhook": "/api/leads/webhook/",
        "status": "online"
    })


urlpatterns = [
    path("", api_root, name="api-root"),
    path("admin/", admin.site.urls),
    path("api/leads/", include("leads.urls")),
]

