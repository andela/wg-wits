# -*- coding: utf-8 -*-

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

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy

from wger.nutrition.forms import MealForm

from django.views.generic import CreateView, UpdateView

from wger.nutrition.models import NutritionPlan, Meal, Ingredient, MealItem
from wger.utils.generic_views import WgerFormMixin

logger = logging.getLogger(__name__)


# ************************
# Old Meal functions
# ************************

class EatenMealCreateView(WgerFormMixin, CreateView):
    '''
    Generic view to add an old meal to a nutrition plan
    '''

    form_class = MealForm
    template_name = 'meal/eaten_meal.html'
    owner_object = {'pk': 'plan_pk', 'class': NutritionPlan}

    def form_valid(self, form):
        plan = get_object_or_404(
            NutritionPlan, pk=self.kwargs['plan_pk'], user=self.request.user)
        form.instance.plan = plan
        form.instance.order = 1
        response = super(EatenMealCreateView, self).form_valid(form)
        ingredient = form.cleaned_data['ingredient']
        request_amount = form.cleaned_data['amount']
        weight_unit = form.cleaned_data['weight_unit']
        new_meal = Meal.objects.get(id=self.object.id)
        new_meal.already_eaten = True
        new_meal.save()
        database_ingredient = Ingredient.objects.get(name=ingredient)
        meal_item = MealItem(
            meal=new_meal,
            ingredient=database_ingredient,
            order=1,
            amount=request_amount,
            weight_unit=weight_unit)
        meal_item.save()
        return response

    def get_success_url(self):
        return self.object.plan.get_absolute_url()

    # Send some additional data to the template
    def get_context_data(self, **kwargs):
        context = super(EatenMealCreateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('nutrition:eaten_meal:add',
                                         kwargs={'plan_pk': self.kwargs['plan_pk']})
        return context
