from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO
from django.contrib.auth.models import User


class CommandsTestCase(TestCase):

    def test_add_rest_api_users(self):
        " Test add-user-rest-api command"
        user = User.objects.create_user(
            'wasswad',
            'wasswad@gmail.com',
            '12345678'
        )
        user.save()

        user_profile = user.userprofile
        user_profile.add_user = True
        user_profile.save()

        out = StringIO()
        args = ['wasswad@gmail.com']
        opts = {'username_or_email': '--username_or_email'}
        call_command('add-user-rest-api', *args, **opts, stdout=out)
        self.assertIn('has been granted permission', out.getvalue())

    def test_add_rest_api_users_without_options(self):
        " Test add-user-rest-api command without options or values should fail"
        out = StringIO()
        call_command('add-user-rest-api', stdout=out)
        self.assertIn('must be specified!', out.getvalue())

    def test_add_rest_api_users_without_username_or_email(self):
        " Test add-user-rest-api command without option must fail"
        user = User.objects.create_user(
            'wasswad',
            'wasswad@gmail.com',
            '12345678'
        )
        user.save()

        user_profile = user.userprofile
        user_profile.add_user = True
        user_profile.save()

        out = StringIO()
        args = []
        opts = {'username_or_email': '--username_or_email'}
        call_command('add-user-rest-api', *args, **opts, stdout=out)
        self.assertIn('No value has been submitted', out.getvalue())

    def test_add_rest_api_users_does_not_exist(self):
        " Test add-user-rest-api command does not exist should fail"
        user = User.objects.create_user(
            'wasswad',
            'wasswad@gmail.com',
            '12345678'
        )
        user.save()

        user_profile = user.userprofile
        user_profile.add_user = True
        user_profile.save()

        out = StringIO()
        args = ['testings@gmail.com']
        opts = {'username_or_email': '--username_or_email'}
        call_command('add-user-rest-api', *args, **opts, stdout=out)
        self.assertIn('does not exist', out.getvalue())
