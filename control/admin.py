from django.contrib import admin

# Register your models here.
from control.models import *

admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(ThirdPartyQueue)
admin.site.register(ThirdPartyCompany)