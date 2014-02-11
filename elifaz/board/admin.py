from board.models import *
from django.contrib.admin import site, ModelAdmin, TabularInline
from chances.admin import PostAdmin, FeatureAdmin

class FeaturePostAdmin(PostAdmin, FeatureAdmin):
    fieldsets = [PostAdmin.fieldsets[0], FeatureAdmin.fieldsets[0],
                 PostAdmin.fieldsets[1]]

class SchedulableFeaturePostAdmin(PostAdmin):
    fieldsets = PostAdmin.get_schedulable_fieldsets(
        'Evento extra da pubblicizzare', 'schedulable_feature')
    
class SchoolEditionPostAdmin(PostAdmin):
    fieldsets = PostAdmin.get_schedulable_fieldsets(
        'Edizione da pubblicizzare', 'edition')

class SchoolModulePostAdmin(PostAdmin):
    fieldsets = PostAdmin.get_schedulable_fieldsets(
        'Modulo da pubblicizzare', 'module')

class SchoolReferencePostAdmin(PostAdmin):
    fieldsets = PostAdmin.get_schedulable_fieldsets(
        'Riferimento da pubblicizzare', 'reference')

site.register(Feature, FeaturePostAdmin)
site.register(SchedulableFeature, SchedulableFeaturePostAdmin)
site.register(SchoolEdition, SchoolEditionPostAdmin)
site.register(SchoolModule, SchoolModulePostAdmin)
site.register(SchoolReference, SchoolReferencePostAdmin)
