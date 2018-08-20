from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO
from django.contrib.auth.models import User
from wger.core.models import APIKeyUsers


class CommandsTestCase(TestCase):

    def test_list_rest_api_users_available(self):
        " Test list-user-rest-api command"
        creator = User.objects.create_user(
            'wasswadero',
            'wasswadero@gmail.com',
            '12345678'
        )
        user = User.objects.create_user(
            'wasswad',
            'wasswad@gmail.com',
            '12345678'
        )
        creator.save()
        user.save()

        creator_profile = creator.userprofile
        creator_profile.add_user = True
        creator_profile.save()

        user_profile = user.userprofile
        user_profile.rest_api_user = True
        user_profile.save()

        api_user = APIKeyUsers.objects.create(user=user, creator=creator)
        api_user.save()

        out = StringIO()
        call_command('list-user-rest-api', stdout=out)
        self.assertIn('Username', out.getvalue())

    def test_list_rest_api_users_not_available(self):
        " Test list-user-rest-api command"
        out = StringIO()
        call_command('list-user-rest-api', stdout=out)
        self.assertIn('No user has not been created via REST API.', out.getvalue())
