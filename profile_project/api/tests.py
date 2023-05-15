from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from profile_project.api.models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.urls import reverse
from rest_framework import status


class ProfileTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()

        # Create a user object
        cls.user = User.objects.create_user(
            username='testuser', password='testpass'
        )

        # Create a profile object
        cls.profile = Profile.objects.create(
            user_id=cls.user.id,
            name='Test User',
            birth_date='2000-01-01',
            bio='This is a test bio.',
            website='http://www.example.com',
            avatar=SimpleUploadedFile(
                name='test_image.png',
                content=open(str(settings.BASE_DIR) + '/test/images/test_image.png', 'rb').read(),
                content_type='image/png'
            )
        )
        cls.url = reverse('profile-detail', args=[cls.profile.id])


    def test_get_absolute_url(self):
        expected_url = reverse('profile-detail', args=[str(self.profile.id)])
        self.assertEqual(self.profile.get_absolute_url(), expected_url)

    def test_bio_contains_text(self):
        self.assertIn('test bio', self.profile.bio.lower())

    def test_website_starts_with_http(self):
        self.assertTrue(self.profile.website.startswith('http'))

    def test_birth_date_format(self):
        self.assertEqual(self.profile.birth_date, '2000-01-01')

    def test_avatar_upload(self):
        self.assertTrue(self.profile.avatar)
        self.assertEqual(self.profile.avatar.name, 'images/test_image.png')

    def test_user_delete_cascade(self):
        user_count = User.objects.filter(id=self.user.id).count()
        self.assertEqual(user_count, 1)

        self.user.delete()

        user_count = User.objects.filter(id=self.user.id).count()
        self.assertEqual(user_count, 0)

        profile_count = Profile.objects.filter(user_id=self.user.id).count()
        self.assertEqual(profile_count, 0)

    def test_get_profile(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.profile.name)
        self.assertEqual(response.data['bio'], self.profile.bio)
        self.assertEqual(response.data['website'], self.profile.website)
        self.assertEqual(response.data['user_id'], self.profile.user_id)

    def test_create_profile(self):
        data = {
            'user_id': self.user.id,
            'name': 'New User',
            'birth_date': '2001-01-01',
            'bio': 'This is a new test bio.',
            'website': 'http://www.newexample.com',
            'avatar': SimpleUploadedFile(
                name='new_test_image.png',
                content=open(str(settings.BASE_DIR) + '/test/images/test_image.png', 'rb').read(),
                content_type='image/png'
            )
        }
        response = self.client.post(reverse('profile-list'), data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 2)
        self.assertEqual(Profile.objects.get(id=2).name, 'New User')

    def test_update_profile(self):
        data = {
            'name': 'Updated User',
            'bio': 'This is an updated test bio.',
            'website': 'http://www.updatedexample.com',
        }
        response = self.client.patch(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.name, 'Updated User')
        self.assertEqual(self.profile.bio, 'This is an updated test bio.')
        self.assertEqual(self.profile.website, 'http://www.updatedexample.com')

    def test_delete_profile(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.count(), 0)

