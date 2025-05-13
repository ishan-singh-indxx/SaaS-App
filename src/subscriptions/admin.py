from django.contrib import admin

# Register your models here.
from .models import SubscriptionModel, UserSubscriptionModel
admin.site.register(SubscriptionModel)
admin.site.register(UserSubscriptionModel)
