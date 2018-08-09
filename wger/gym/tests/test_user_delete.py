
from django.core.urlresolvers import reverse
from wger.core.tests.base_testcase import WorkoutManagerTestCase
from wger.gym.models import GymAdminConfig


class GymDeleteUserTestCase(WorkoutManagerTestCase):

    def delete_user(self, fail=False, logged_in=True):
        GymAdminConfig.objects.all().delete()

        self.client.post(reverse('gym:gym:add-user', kwargs={'gym_pk': 1}),
                         {'first_name': 'Cletus',
                          'last_name': 'Spuckle',
                          'username': 'cletus',
                          'email': 'cletus@spuckle-megacorp.com',
                          'role': 'admin'})

        user = GymAdminConfig.objects.first()

        user_pk = user.pk if user else 4
        response = self.client.post(
            reverse('gym:gym:delete-user', kwargs={'user_pk': user_pk}))

        if logged_in:
            if fail:
                self.assertEqual(response.status_code, 403)
            else:
                self.assertEqual(response.status_code, 302)
        else:
            self.assertEqual(response.status_code, 302)

    def test_delete_user_authorized(self):
        """
        Tests deleting a user an authorized user
        """
        self.user_login('admin')
        self.delete_user()

    def test_delete_user_unauthorized(self):
        """
        Tests deleting a user an unauthorized user
        """
        self.user_login('test')
        self.delete_user(fail=True)

    def test_delete_user_not_logged_in(self):
        """
        Tests deleting a user an unauthorized user
        """
        self.delete_user(fail=True, logged_in=False)
