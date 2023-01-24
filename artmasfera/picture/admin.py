from django.contrib import admin

from .models import *

class MasterClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'activation', 'date_mk', 'time_mk', 'local', 'name_picture')
    list_display_links = ('id',)
    search_fields = ('date_mk', 'local')
    list_editable = ('activation',)
    list_filter = ('view_of_clients', 'activation', 'local')

class MasterClassClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_guest', 'name_picture')
    list_display_links = ('id',)
class Gallery_pictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_picture',)
    list_display_links = ('id', 'name_picture')

admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(MasterClass_Clients, MasterClassClientsAdmin)
admin.site.register(Gallery_picture, Gallery_pictureAdmin)