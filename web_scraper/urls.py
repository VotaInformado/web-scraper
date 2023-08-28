# Django
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import include, path

# Project
from web_scraper.views import ScraperView

router = SimpleRouter()

router.register(r"", ScraperView, basename="legislators")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
