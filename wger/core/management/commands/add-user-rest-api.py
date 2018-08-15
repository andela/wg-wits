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
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    '''
    Wger REST API consumers that want to create users are given permissions to
    create users users via the REST API on demand.
    '''

    option_list = BaseCommand.option_list + (
        make_option(
            '--username_or_email',
            action='store_true',
            dest='username_or_email',
            default=False,
            help='username of user to receive permissions'
        ),
    )

    help = ('Grants a user permission to create users via Wger REST API')

    def grant_permission(self, user, user_obj):
        if user is None:
            self.stdout.write('{} does not exist.' . format(user_obj))
            return
        user_profile = user.userprofile
        user_profile.add_user = True
        user_profile.save()

        self.stdout.write(
            '{} has been granted permission to add users via REST API.'.format(user_obj)
        )

    def handle(self, *position_args, **options):
        # Emphasize that the command should provide atleast one of these options
        if options.get('username_or_email') is False:
            self.stdout.write('Option --username_or_email must be specified!')
            return

        if len(position_args) < 1:
            self.stdout.write('No value has been submitted.')
            return

        # Check if the user submitted email
        username_or_email = str(position_args[0])
        user = User.objects.filter(
            Q(username=username_or_email) | Q(email=username_or_email)
        ).first()
        self.grant_permission(user, username_or_email)
