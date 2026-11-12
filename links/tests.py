from django.test import TestCase

class HealthTest(TestCase):
    def test_health(self):
        self.assertEqual(self.client.get("/health").status_code,301)
        
    def test_health_301(self):
        self.assertEqual(self.client.get("/health").status_code,301)
    
    def test_duplicate_url_returns_409(self):
        body = {"long_url": "https://www.instagram.com/p/DZ-AORszRRS/"}
        self.client.post("/v1/urls/create/", body, content_type="application/json")
        r = self.client.post("/v1/urls/create/", body, content_type="application/json")
        self.assertEqual(r.status_code, 409)