from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagersTests(TestCase):
    def setUp(self):
        # user model instance for testing
        self.User = get_user_model()

    def test_create_user(self):
        # regular user using the create_user method from the custom manager
        user = self.User.objects.create_user(
            email='winchygichu@gmail.com',
            password='winchy.#testpassworD',
            company_name='MyCompany',
            company_address='Company Address',
            industry='Tech',
            employee_count=50,
            contact_person_name='John Doe',
            contact_email='john@example.com',
            phone_number='1234567890',
            subdomain='mycompany'
        )

        # Assertions to check user attributes
        self.assertEqual(user.email, 'winchygichu@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        # username should be None for the custom user model
        self.assertIsNone(user.username)

        # Test exceptions when creating a user
        with self.assertRaises(ValueError):
            # Missing required fields
            self.User.objects.create_user()

        with self.assertRaises(ValueError):
            # Missing email field
            self.User.objects.create_user(
                email='',
                password='password',
                company_name='MyCompany',
                company_address='Company Address',
                industry='Tech',
                employee_count=50,
                contact_person_name='John Doe',
                contact_email='john@example.com',
                phone_number='1234567890',
                subdomain='mycompany'
            )

        with self.assertRaises(ValueError):
            # Missing password field
            self.User.objects.create_user(
                email='winchygichu@gmail.com',
                password='',
                company_name='MyCompany',
                company_address='Company Address',
                industry='Tech',
                employee_count=50,
                contact_person_name='John Doe',
                contact_email='john@example.com',
                phone_number='1234567890',
                subdomain='mycompany'
            )

    def test_create_superuser(self):
        # Create a superuser using the create_superuser method from your custom manager
        admin_user = self.User.objects.create_superuser(
            email="super@user.com",
            password="winchy.hub"
        )

        # Assertions for superuser attributes
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        # username should be None for the custom user model
        self.assertIsNone(admin_user.username)

        # Test exception when creating a superuser with is_superuser=False
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                email="super@user.com", password="winchy.hub", is_superuser=False)
