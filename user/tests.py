from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def test_create_user_and_login(self):
        User.objects.create_user(username='john', email='test_create_user@gmail.com', password='smith')
        registered_user = User.objects.get(username='john')
        self.assertEqual(registered_user.username, 'john')
        self.assertEqual(registered_user.email, 'test_create_user@gmail.com')

        c = Client()
        response = c.post('/login', {'username': 'john', 'password': 'smith'})
        status_code = response.status_code
        self.assertIn('_auth_user_id', c.session)
        self.assertEqual(status_code, 302)


    def test_incorrect_login_details(self):
        c = Client()
        response = c.post('/login', {'username': 'john1', 'password': 'smith1'})
        status_code = response.status_code
        self.assertContains(response, 'Неправильні дані!')
        self.assertEqual(status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

