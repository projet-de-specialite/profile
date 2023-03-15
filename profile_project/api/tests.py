from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

class ProfileTestCase(APITestCase):
    def test_create_profile(self):
        # Using the standard RequestFactory API to create a form POST request
        factory = APIRequestFactory()
        request = factory.post('/profiles/',
            {
            "avatar": "https://pedag.u-picardie.fr/moodle/upjv/pluginfile.php/1/core_admin/logocompact/300x300/1677060056/Logo_UPJV_navbar.png",
            "bio": "Hello",
            "birth_date": "01/02/1997",
            "created_on": "2023-03-15T07:08:43.233477Z",
            "id": 1,
            "name": "Mouad",
            "user_id": 1,
            "username": "mouaddb",
            "website": "mouad.ma"
            }
        )

