from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is BharatFD?", answer="BharatFD brings you up-to-date interest rates, flexible terms, and the security of trusted banks—all in one place. ... Access FD rates 30-40% higher than standard options—because you deserve more.")

    def test_faq_creation(self):
        faq = FAQ.objects.get(question="What is BharatFD?")
        self.assertEqual(faq.answer, "BharatFD brings you up-to-date interest rates, flexible terms, and the security of trusted banks—all in one place. ... Access FD rates 30-40% higher than standard options—because you deserve more.")
