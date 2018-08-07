from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from wger.nutrition.models import NutritionPlan, Meal, MealItem
from django.core.cache import cache
from wger.utils.cache import cache_mapper


@receiver(post_save, sender=NutritionPlan)
@receiver(post_delete, sender=NutritionPlan)
@receiver(post_delete, sender=MealItem)
@receiver(post_save, sender=MealItem)
@receiver(post_save, sender=Meal)
@receiver(post_delete, sender=Meal)
def reset_nutrional_plan_canonical(sender, **kwargs):
    '''
    Function to send signal
    '''
    instance_sender = kwargs['instance']
    if isinstance(instance_sender, (MealItem, NutritionPlan, Meal)):
        cache.delete(cache_mapper.get_nutritional_plan_canonical(
            instance_sender.get_owner_object().id))
