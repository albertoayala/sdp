from django.contrib import admin
from thermostats.models import BaseControl, Thermostat

class BaseControlAdmin(admin.ModelAdmin):
	fieldsets = [
		('Settings', {'fields': ['account_id', 'basecontrol_id', 'name']}),
		('Temperature Control', {'fields':['current_temperature', 'setpoint_temperature', 'setback_temperature', 'status']}),
	]
	list_display = ('name', 'account_id', 'basecontrol_id')
	search_fields = ['name']

class ThermostatAdmin(admin.ModelAdmin):
	fieldsets = [
		('Settings', {'fields': ['base_control','account_id', 'thermostat_id', 'name']}),
		('Temperature Control', {'fields':['current_temperature', 'setpoint_temperature', 'setback_temperature', 'status']}),
	]
	list_display = ('name', 'base_control', 'account_id', 'thermostat_id')
	search_fields = ['name']

admin.site.register(BaseControl, BaseControlAdmin)
admin.site.register(Thermostat, ThermostatAdmin)