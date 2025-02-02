from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FAQ

@receiver(post_save, sender=FAQ)
def clear_faq_cache(sender, instance, **kwargs):
    """Clears Redis cache when an FAQ is updated."""
    from django.core.cache import cache
    for lang in ['en', 'hi', 'bn']:
        cache_key = f"faqs_{lang}"
        cache.delete(cache_key)
