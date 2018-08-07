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
from django.core.cache import cache

from wger.nutrition.models import NutritionPlan, Meal, MealItem
from wger.utils.cache import cache_mapper
from wger.core.tests.base_testcase import WorkoutManagerTestCase


class NutritionPlanCacheTestCase(WorkoutManagerTestCase):
    '''
    Test case for the NutritionalPlan canonical representation
    '''
    def test_nutritional_plan_canonical_form_cache(self):
        '''
        Test that the nuttritional plan cache is correctly generated
        '''
        self.assertFalse(cache.get(cache_mapper.get_nutritional_plan_canonical(1)))
        nutritional_plan = NutritionPlan.objects.get(pk=1)
        nutritional_plan.get_nutritional_values()
        self.assertTrue(cache.get(cache_mapper.get_nutritional_plan_canonical(1)))

    def test_nutritional_plan_canonical_form_cache_save(self):
        '''
        Tests the nutritional_plan values cache when saving a nutritional plan
        '''
        nutritional_plan = NutritionPlan.objects.get(pk=1)
        nutritional_plan.get_nutritional_values()
        self.assertTrue(cache.get(cache_mapper.get_nutritional_plan_canonical(1)))

        nutritional_plan.save()
        self.assertFalse(cache.get(cache_mapper.get_nutritional_plan_canonical(1)))

    def test_nutritional_plan_canonical_form_cache_delete(self):
        '''
        Tests the nutrional plan values cache when deleting
        '''
        nutritional_plan = NutritionPlan.objects.get(pk=1)
        nutritional_plan.get_nutritional_values()
        self.assertTrue(cache.get(cache_mapper.get_nutritional_plan_canonical(1)))

        nutritional_plan.delete()
        self.assertFalse(cache.get(cache_mapper.get_workout_canonical(1)))
