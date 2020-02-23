from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class IpAPIViewTestCase(TestCase):
    """ os API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_os_api', password='Ty8sCsWifIJmxx4KaJd6')

    def test_os_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/oss/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_os_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_os_api', password='Ty8sCsWifIJmxx4KaJd6')
        # get response
        response = self.client.get('/api/oss/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_os_list_api_method_post(self):
        """ POST is allowed """

        # login testuser
        login = self.client.login(username='testuser_os_api', password='Ty8sCsWifIJmxx4KaJd6')
        # create POST string
        poststring = {"os_name": "os_api_1"}
        # get response
        response = self.client.post('/api/oss/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_os_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_os_api', password='Ty8sCsWifIJmxx4KaJd6')
        # create url
        destination = urllib.parse.quote('/api/oss/', safe='/')
        # get response
        response = self.client.get('/api/oss', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_os_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_os_api', password='Ty8sCsWifIJmxx4KaJd6')
#        # get response
#        response = self.client.get('/api/oss/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_os_api')
