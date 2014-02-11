from django.contrib.admin import ModelAdmin


class NoteAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'slug']}),
        ('Contenuti testuali',
         {'fields': ['label', 'title', 'subtitle', 'description']})
    ]

    @classmethod
    def get_fields_from_fieldsets(cls):
        return [field for sublist in [fieldset[1]['fields'] \
                                          for fieldset in cls.fieldsets] \
                    for field in sublist]


class SchedulableAdmin(NoteAdmin):
    ordering = ['datetime', 'slug',]
    list_display = ['__unicode__', 'name', 'slug', 'title',]
    fieldsets = [
        NoteAdmin.fieldsets[0], 
        ('Tempi', {'fields': ['datetime', 'display_datetime']}),
        ('Luoghi', {'fields': ['venue']}),
        NoteAdmin.fieldsets[1]
    ]


class PostAdmin(NoteAdmin):
    ordering = ['published', 'slug']
    list_display = ['name', 'slug', 'published',]
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'published']}),
        NoteAdmin.fieldsets[1],
    ]

    @classmethod
    def get_schedulable_fieldsets(cls, fieldset_name, field):
        return [cls.fieldsets[0], (fieldset_name, {'fields': [field]}),
                cls.fieldsets[1]]
        

class FeatureAdmin(ModelAdmin):
    fieldsets = [('Risorsa extra', {'fields': ['url']})]
