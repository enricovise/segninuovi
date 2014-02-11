from scuoladsc.models import *
from django.contrib.admin import site, ModelAdmin, TabularInline
from chances.admin import SchedulableAdmin
from django import forms

class PathSchedulableAdmin(SchedulableAdmin):
    id_field = 'name'
    list_display_links = [id_field,]
    list_display = ['path', 'datetime', id_field]




class ReferenceAdminForm(forms.ModelForm):
    class Meta:
        model = Reference

    @staticmethod
    def xor(a, b):
        return (a and not b) or (b and not a)
    
    def clean(self):
        data = super(ReferenceAdminForm, self).clean()
        if not ReferenceAdminForm.xor(data.get('call'), data.get('speaker')):
            raise forms.ValidationError('Specify either a call or a speaker.')
        return data

class ReferenceAdmin(PathSchedulableAdmin):
    form = ReferenceAdminForm
    fieldsets = [
        (None, {'fields': ['call', 'speaker', 'material', 'name', 'slug']}),
        PathSchedulableAdmin.fieldsets[3],
        ('Ordine', {'fields': ['datetime']})
    ]

class ReferenceInline(TabularInline):
    model = Reference
    extra = 1
    fields = ['material', 'name', 'slug']

class CallReferenceInline(ReferenceInline):
    fk_name = 'call'

class SpeakerReferenceInline(ReferenceInline):
    fk_name = 'speaker'

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(SpeakerReferenceInline, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

        if db_field.name == 'material':
            field.queryset = field.queryset.filter(
                authors=request.speaker.person) if request.speaker else \
                field.queryset.none()

        return field




class SpeakerAdmin(PathSchedulableAdmin):
    fieldsets = [(None, {'fields': ['call', 'person', 'name', 'slug',]})]
    inlines = [SpeakerReferenceInline,]

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request.speaker = obj
        return super(SpeakerAdmin, self).get_form(request, obj, **kwargs)

class SpeakerInline(TabularInline):
    model = Speaker
    extra = 1
    fk_name = 'call'
    fields = SpeakerAdmin.get_fields_from_fieldsets()




class CallAdmin(PathSchedulableAdmin):
    fieldsets = [
        (None, {'fields': ['module', 'datetime', 'display_datetime', 'name', 'slug']}),
        PathSchedulableAdmin.fieldsets[3]
    ]
    inlines = [SpeakerInline, CallReferenceInline,]

class CallInline(TabularInline):
    model = Call
    fk_name = 'module'
    extra = 1
    fields = CallAdmin.get_fields_from_fieldsets()[:-2]




class ModuleAdmin(PathSchedulableAdmin):
    fieldsets = [
        (None, {'fields': ['edition', 'name', 'slug']}),
        ('Dettagli', {'fields': ['label', 'title', 'venue']})
    ]
    inlines = [CallInline,]

class ModuleInline(TabularInline):
    model = Module
    fk_name = 'edition'
    extra = 1
    fields = ModuleAdmin.get_fields_from_fieldsets()




class EditionAdmin(PathSchedulableAdmin):
    inlines = [ModuleInline,]
    fieldsets = [PathSchedulableAdmin.fieldsets[0], PathSchedulableAdmin.fieldsets[3]]




site.register(Edition, EditionAdmin)
site.register(Module, ModuleAdmin)
site.register(Call, CallAdmin)
site.register(Speaker, SpeakerAdmin)
site.register(Reference, ReferenceAdmin)
