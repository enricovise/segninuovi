from extra.models import SchedulableFeature
from django.contrib.admin import site
from chances.admin import SchedulableAdmin, FeatureAdmin

class SchedulableFeatureAdmin(SchedulableAdmin, FeatureAdmin):
    fieldsets = [SchedulableAdmin.fieldsets[0],
                 FeatureAdmin.fieldsets[0]] + SchedulableAdmin.fieldsets[1:]

site.register(SchedulableFeature, SchedulableFeatureAdmin)
