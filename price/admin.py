from django.contrib import admin
from .models import PriceTable,PriceCard
# Register your models here.
admin.site.register(PriceCard)
admin.site.register(PriceTable)