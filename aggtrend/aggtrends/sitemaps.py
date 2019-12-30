from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings


class StaticSitemap(Sitemap):
    def items(self):
        return [
            "html-code-examples",
            "css-code-examples",
            "javascript-code-examples",
            "list",
            "privacy",
            "about",
            "affiliations",
           
           
        ]

    def location(self, item):
        if isinstance(item, tuple):
            return reverse(item[0], kwargs=item[1])
        return reverse(item)

