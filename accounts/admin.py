from django.contrib import admin
from accounts.models import User, Publisher, Manager, Owner
# Register your models here.
admin.site.register(User)
admin.site.register(Publisher)
admin.site.register(Manager)
admin.site.register(Owner)
