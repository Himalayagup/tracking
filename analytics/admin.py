from django.contrib import admin

from analytics.models import ObjectLead, ObjectViewed, UniqueID

# Register your models here.
admin.site.register(ObjectViewed)
admin.site.register(ObjectLead)
admin.site.register(UniqueID)
