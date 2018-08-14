from django.core.urlresolvers import reverse
from wger.core.tests.base_testcase import WorkoutManagerTestCase
from wger.gym.models import GymAdminConfig
from django.contrib.auth.models import User


class GymAddExistingUserTestCase(WorkoutManagerTestCase):
    '''
    Tests admin adding users to gyms
    '''
    def add_existing_user(self, fail=False, logged_in=True, role='admin'):
        '''
        Helper function to add users
        '''
        GymAdminConfig.objects.all().delete()

        self.client.post(reverse('gym:gym:add-user', kwargs={'gym_pk': 1}),
                         {'first_name': 'Cletus',
                          'last_name': 'Spuckle',
                          'username': 'cletus',
                          'email': 'cletus@spuckle-megacorp.com',
                          'role': str(role)})

        user = GymAdminConfig.objects.first()
        if not fail:
            user_pk = user.user_id if user else 4
            self.client.post(
                reverse('gym:gym:delete-user', kwargs={'user_pk': user_pk}))

        response = self.client.post(reverse('gym:gym:add-user-existing', kwargs={'gym_pk': 1}),
                                    {'username': 'cletus', 'role': str(role)})

        if fail:
            self.assertEqual(response.status_code, 403)
        else:
            self.assertEqual(response.status_code, 302)

    def test_delete_user_authorized(self):
        """
        Tests deleting a user an authorized user
        """
        self.user_login('admin')
        self.add_existing_user()

    def test_delete_user_unauthorized(self):
        """
        Tests deleting a user an unauthorized user
        """
        self.user_login('test')
        self.add_existing_user(fail=True)

    def test_delete_user_not_logged_in(self):
        """
        Tests deleting a user an unauthorized user
        """
        self.add_existing_user(fail=True, logged_in=False)
