# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License


from rest_framework.test import (
    APIClient,
    APITestCase
)
from wger.core.tests.base_testcase import WorkoutManagerTestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class CreateUserRESTAPITest(APITestCase, WorkoutManagerTestCase):
    '''
    Tests creating users via REST API
    '''

    def test_get_created_users(self):
        '''
        Retrieve users
        '''
        user = User.objects.get(username='demo')

        self.user_login('demo')

        api_key = Token.objects.get(user=user)

        test_client = APIClient()
        test_client.credentials(HTTP_AUTHORIZATION='Token ' + api_key.key)
        register = test_client.get('/api/v2/users/')
        self.assertEqual(200, register.status_code)

    def test_create_user(self):
        '''
        Create user via REST API
        '''
        user = User.objects.get(username='demo')

        self.user_login('demo')

        api_key = Token.objects.get(user=user)

        test_client = APIClient()
        test_client.credentials(HTTP_AUTHORIZATION='Token ' + api_key.key)
        payload = {
            "username": "RESTAPIUSER",
            "email": "restapiuser@gmail.com",
            "password": "12345678"
        }

        response = test_client.post('/api/v2/users/', data=payload, format='json')
        self.assertEqual(201, response.status_code)

    def test_create_user_without_permission(self):
        '''
        Create user via REST API
        '''
        user = User.objects.get(username='test')

        self.user_login('test')

        api_key = Token.objects.get(user=user)

        test_client = APIClient()
        test_client.credentials(HTTP_AUTHORIZATION='Token ' + api_key.key)
        payload = {
            "username": "RESTAPIUSER",
            "email": "restapiuser@gmail.com",
            "password": "12345678"
        }

        response = test_client.post('/api/v2/users/', data=payload, format='json')
        self.assertEqual(403, response.status_code)

    def test_create_user_exists(self):
        '''
        Create user via REST API exists should not fail.
        '''
        user = User.objects.get(username='demo')

        self.user_login('demo')

        api_key = Token.objects.get(user=user)

        test_client = APIClient()
        test_client.credentials(HTTP_AUTHORIZATION='Token ' + api_key.key)
        payload = {
            "username": "RESTAPIUSER",
            "email": "restapiuser@gmail.com",
            "password": "12345678"
        }

        payload_exists = {
            "username": "RESTAPIUSER",
            "email": "restapiuser@gmail.com",
            "password": "12345678"
        }

        test_client.post('/api/v2/users/', data=payload, format='json')
        response = test_client.post('/api/v2/users/', data=payload_exists, format='json')
        self.assertEqual(400, response.status_code)
