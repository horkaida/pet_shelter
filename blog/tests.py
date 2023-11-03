from django.test import TestCase, Client
from django.urls import reverse
import blog.models


class TestBlog(TestCase):
    fixtures = ["all_data.json"]

    def test_get_all_posts(self):
        c = Client()
        all_posts = blog.models.BlogPost.objects.all().values()
        blog_titles = [post['title'] for post in all_posts]
        response = c.get(reverse('get_all_posts'))
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        for title in blog_titles:
            self.assertIn(title, response.content.decode('utf-8'))

    def test_get_post(self):
        c = Client()
        post = blog.models.BlogPost.objects.filter(id=2).first()
        response = c.get(reverse('get_post', kwargs={'post_id': post.id}))
        status_code = response.status_code
        is_post = post.title in response.content.decode('utf-8')
        self.assertEqual(status_code, 200)
        self.assertTrue(is_post)
