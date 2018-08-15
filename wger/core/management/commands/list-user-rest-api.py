# -*- coding: utf-8 *-*

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

import requests
import os

from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from wger.core.models import APIKeyUsers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Command(BaseCommand):
    '''
    Retrieving all the users created by a user via REST API
    '''

    help = ('Listing REST API users')

    def handle(self, *positional_args, **options):

        wger_users = User.objects.all()
        api_users = []
        for user in wger_users:
            if user.userprofile.rest_api_user:
                api_users.append(user)

        if len(api_users) == 0:
            self.stdout.write('No user has not been created via REST API.')

        for user in api_users:
            self.stdout.write(
                self.style.SUCCESS('Username: {} , Email: {}' . format(user.username, user.email))
            )
