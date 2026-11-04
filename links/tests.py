from django.test import TestCase

class HealthTest(TestCase):
    def test_health(self):
        self.assertEqual(self.client.get("/health").status_code,200)
        
    def test_health_301(self):
        self.assertEqual(self.client.get("/health").status_code,301)
        