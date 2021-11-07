from django.contrib import admin
from .models import User, Station, Cycle

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'date_created')

class stationAdmin(admin.ModelAdmin):
    list_display = ('station_id', 'station_name')

class cycleAdmin(admin.ModelAdmin):
    list_display = ('cycle_id', 'borrowed_user','station_id')

admin.site.register(User, userAdmin)
admin.site.register(Station, stationAdmin)
admin.site.register(Cycle, cycleAdmin)
