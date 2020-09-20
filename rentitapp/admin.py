from django.contrib import admin,messages
from django.db import connection

from .models import Profile, Vehicles
from django.utils.translation import ngettext
admin.site.register(Profile)

def make_published(self,request,queryset):
    updated = queryset.update(status=True)
    self.message_user(request,ngettext('%d Selected items approved for posting','%d success',updated,) % updated,
                      messages.SUCCESS)
    make_published.short_description = "Move the selected items to products table"


class VehiclesAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        qs = super( VehiclesAdmin , self ).get_queryset(request)
        return qs.filter( status=False )

    list_display = ('tov','Adtitle','brand','cost','DOM','S_desc','img1','status')
    actions =[make_published]


admin.site.register(Vehicles, VehiclesAdmin)
