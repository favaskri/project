from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from  e_com.models import Product

class TestUrls(TestCase):

    def setUp(self):
        # Setup a user for login and authenticated views, if necessary
        self.user = User.objects.create_user(username='favaskri@gmail.com', password='Aydin@123')

    def test_home_page(self):
        # Test the home page URL
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        # Test the add product page URL (requires login)
        self.client.login(username='favaskri@gmail.com', password='Aydin@123')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)

    def test_edit_product(self):
        # Create a dummy product to edit (example product model)
        product = Product.objects.create(name="Test Product", price=100)
        
        # Test the edit product page URL
        self.client.login(username='favaskri@gmail.com', password='Aydin@123')
        response = self.client.get(reverse('edit_product', args=[product.pk]))
        self.assertEqual(response.status_code, 200)

    def test_product_details(self):
        product = Product.objects.create(name="Test Product", price=100)
        
        # Log in the user
        self.client.login(username='favaskri@gmail.com', password='Aydin@123')
        
        response = self.client.get(reverse('product_details', args=[product.pk]))
        
        # Check for a redirect
        self.assertEqual(response.status_code, 200)


    def test_delete_product(self):
        product = Product.objects.create(name="Test Product", price=100)
        
        self.client.login(username='favaskri@gmail.com', password='Aydin@123')
        response = self.client.get(reverse('delete_product', args=[product.pk]))
        
        # Check if the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)
        # Optionally, follow the redirect and check the final status
        follow_response = self.client.get(response.url)
        self.assertEqual(follow_response.status_code, 200)


    def test_register(self):
        # Test the registration page URL
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # Test the login page URL
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
    # Login first
        self.client.login(username='favaskri@gmail.com', password='Aydin@123')
        
        # Use POST method instead of GET
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Logout usually redirects

