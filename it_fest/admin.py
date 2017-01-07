from django.contrib import admin
from .models import Participant, Registration


class ParticipantInline(admin.TabularInline):
    model = Participant


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'mobile_number',
                    'institute', 'get_payment_status']
    list_filter = ['institute']
    search_fields = ['full_name', 'mobile_number', 'registration__id']

    def get_payment_status(self, object):
        return object.registration.payment_status
    get_payment_status.short_description = 'Payment Status'


class RegistrationAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline, ]
    search_fields = ['id', 'transaction_id', 'participant__mobile_number']
    list_filter = ['game_name', 'payment_status', ]
    list_display = ['id', 'payment_status', 'bkash_mobile_number',
                    'transaction_id', 'game_name', 'get_institute']

    def get_institute(self, object):
        return object.participant_set.all()[0].institute

    get_institute.short_description = 'Institute'

# Register your models here.
admin.site.register(Participant, ParticipationAdmin)
admin.site.register(Registration, RegistrationAdmin)
