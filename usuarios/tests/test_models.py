from django.test import TestCase
from model_mommy import mommy
from usuarios.models import CustomUser


class UserManagerTestCase(TestCase):
     
    def setUp(self):
        self.user_manager = CustomUser.objects
    
    
    def test_create_user(self):
        email='testuser@exemplo.com'
        password='testpassword'

        user = self.user_manager.create_user(email=email, password=password)
        
        self.assertEqual(str(user), email)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.is_superuser, False)
    
    
    def test_create_user_without_email(self):
        password='testpassword'

        with self.assertRaises(ValueError) as err:
            user = self.user_manager._create_user(email=None, password=password)
        
        self.assertEqual(str(err.exception), 'É necessário informar um e-mail!')
    
    
    def test_create_superuser(self):
        email='testuser@exemplo.com'
        password='testpassword'

        user = self.user_manager.create_superuser(email=email, password=password)

        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)


    def test_create_superuser_is_staff(self):
        email='testuser@exemplo.com'
        password='testpassword'


        with self.assertRaises(ValueError) as err:
            user = self.user_manager.create_superuser(email=email, password=password, is_staff=False)
        
        self.assertEqual(str(err.exception), 'is_staff precisa ser True')
    
    def test_create_superuser_is_superuser(self):
        email='testuser@exemplo.com'
        password='testpassword'

        with self.assertRaises(ValueError) as err:
            user = self.user_manager.create_superuser(email=email, password=password, is_superuser=False)
        
        self.assertEqual(str(err.exception), 'is_superuser precisa ser True')



class CustomUserTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(CustomUser, username='testuser@exemplo.com', email='testuser@exemplo.com')

    
    def test_str(self):
        self.assertEqual(str(self.user), self.user.email)
