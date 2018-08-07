
from django.core.urlresolvers import reverse
from wger.core.tests.base_testcase import WorkoutManagerTestCase
from wger.gym.models import GymAdminConfig


class GymDeleteUserTestCase(WorkoutManagerTestCase):

    def activate_user(self, fail=False, activate=True, logged_in=True):
        GymAdminConfig.objects.all().delete()

        self.client.post(reverse('gym:gym:add-user', kwargs={'gym_pk': 1}),
                         {'first_name': 'Cletus',
                          'last_name': 'Spuckle',
                          'username': 'cletus',
                          'email': 'cletus@spuckle-megacorp.com',
                          'role': 'admin'})

        user = GymAdminConfig.objects.first()

        user_pk = user.pk if user else 4

        if activate:
            url = reverse('gym:gym:activate-user', kwargs={'user_pk': user_pk}) + '?active=true'
            response = self.client.post(url)
        else:
            url = reverse('gym:gym:activate-user', kwargs={'user_pk': user_pk}) + '?active=false'
            response = self.client.post(url)

        if logged_in:
            if fail:
                self.assertEqual(response.status_code, 403)
            else:
                self.assertEqual(response.status_code, 302)
        else:
            self.assertEqual(response.status_code, 302)

    def test_activate_user_authorized(self):
        """
        Tests activating a user an authorized user
        """
        self.user_login('admin')
        self.activate_user()

    def test_deactivate_user_authorized(self):
        """
        Tests activating a user an authorized user
        """
        self.user_login('admin')
        self.activate_user(activate=False)

    def test_activate_user_unauthorized(self):
        """
        Tests activating a user an unauthorized user
        """
        self.user_login('test')
        self.activate_user(fail=True)

    def test_activate_user_not_logged_in(self):
        """
        Tests activating a user an unauthorized user
        """
        self.activate_user(fail=True, logged_in=False)
