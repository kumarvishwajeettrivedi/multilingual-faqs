from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):

    def setUp(self):
        FAQ.objects.create(question="What is BharatFD?", answer="BharatFD offers FD rates higher than standard options.")
        FAQ.objects.create(question="How do I invest in BharatFD?", answer="You can start by signing up on the platform and choosing an FD plan.")

    def test_faq_creation(self):
        """Test if FAQ objects are created correctly"""
        faq = FAQ.objects.get(question="What is BharatFD?")
        self.assertEqual(faq.answer, "BharatFD offers FD rates higher than standard options.")

    def test_multiple_faqs(self):
        """Test retrieving multiple FAQs"""
        faqs = FAQ.objects.all()
        self.assertEqual(faqs.count(), 2) 

    def test_empty_faq(self):
        """Test behavior when no FAQs exist"""
        FAQ.objects.all().delete()
        faqs = FAQ.objects.all()
        self.assertEqual(faqs.count(), 0)

    def test_faq_string_representation(self):
        """Test if the FAQ model's string representation works correctly"""
        faq = FAQ.objects.get(question="What is BharatFD?")
        self.assertEqual(str(faq), "What is BharatFD?")

