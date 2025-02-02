from celery import shared_task
from .models import FAQ

@shared_task
def translate_faq(faq_id):
    """Asynchronously translates FAQ content."""
    faq = FAQ.objects.get(id=faq_id)
    faq.save() 
