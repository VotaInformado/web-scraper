from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from web_scraper.utils import Scraper


class ScraperView(viewsets.GenericViewSet):
    @action(methods=["GET"], detail=False)
    def status(self, request):
        return Response({"status": "ok"})

    @action(methods=["POST"], detail=False, url_path="scrape-page")
    def scrape_page(self, request):
        year = request.data["year"]
        content = Scraper.scrape_page(year)
        return Response({"content": content})
