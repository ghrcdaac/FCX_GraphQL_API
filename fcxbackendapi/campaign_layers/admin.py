from django.contrib import admin

# Register your models here.

from .models import Link, DOI, Legend, InstrumentLayer, CampaignLayer

admin.site.register(Link)
admin.site.register(DOI)
admin.site.register(Legend)
admin.site.register(InstrumentLayer)
admin.site.register(CampaignLayer)