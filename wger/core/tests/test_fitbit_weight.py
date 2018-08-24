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

import logging
import requests
import base64
import os
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from wger.core.tests.base_testcase import (
    WorkoutManagerTestCase,
    WorkoutManagerEditTestCase,
    WorkoutManagerAccessTestCase
)
logger = logging.getLogger(__name__)


class UserWeightFitbitTestCase(WorkoutManagerTestCase):
    def test_weight_fitbit_data(self):
        client_id = os.environ.get('FITBIT_WEIGHT_CLIENT_ID')
        client_secret = os.environ.get('FITBIT_WEIGHT_CLIENT_SECRET')
        headers = {
            'Authorization': 'Basic ' +
            base64.b64encode((client_id + ":" + client_secret).encode('UTF-8')).decode('ascii'),
            'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.get('https://api.fitbit.com/1/user/6T3GXD/profile.json',
                           headers=headers).json()

        self.assertIsInstance(res, dict)

    def test_exercise_fitbit_data(self):
        client_id = os.environ.get('FITBIT_EXERCISE_CLIENT_ID')
        client_secret = os.environ.get('FITBIT_EXERCISE_CLIENT_SECRET')
        headers = {
            'Authorization': 'Basic ' +
            base64.b64encode((client_id + ":" + client_secret).encode('UTF-8')).decode('ascii'),
            'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.get('https://api.fitbit.com/1/user/6T3GXD/profile.json',
                           headers=headers).json()

        self.assertIsInstance(res, dict)
