from django.test import TestCase

from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    def test_home_page_url(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
    def test_home_page_content(self):
        response=self.client.get(reverse('home'))
        self.assertContains(response,'homepage')
    def test_home_page_templates(self):
        resopnse=self.client.get(reverse('home'))
        self.assertTemplateUsed(resopnse, 'home.html')

class AboutUsPageTest(TestCase):
    def test_about_us_page_by_name(self):
        response=self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code,200)
    def test_about_us_page_url(self):
        response=self.client.get('/aboutus/')
        self.assertEqual(response.status_code,200)
    def test_about_page_content(self):
        resopnse=self.client.get(reverse('aboutus'))
        self.assertContains(resopnse,'about')
    def test_about_page_templtes(self):
        resopnse=self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(resopnse, 'pages/about.html')