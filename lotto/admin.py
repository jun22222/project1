from django.contrib import admin

# Register your models here.
from lotto.models import GuessNumbers, Location

admin.site.register(GuessNumbers)
admin.site.register(Location)