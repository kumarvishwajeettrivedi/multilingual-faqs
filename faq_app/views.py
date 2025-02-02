from rest_framework import generics
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f"faqs_{lang}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        faqs = FAQ.objects.all()
        data = [faq.get_translated(lang) for faq in faqs]
        cache.set(cache_key, data, timeout=3600)  
        return faqs
