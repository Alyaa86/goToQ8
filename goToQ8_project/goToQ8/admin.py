from django.contrib import admin
from .models import (
	Event,
	Plan,
	Favourite,
	Friends,
	Profile
	)

# Register your models here.
admin.site.register(Event)
admin.site.register(Plan)
admin.site.register(Favourite)
admin.site.register(Friends)
admin.site.register(Profile)