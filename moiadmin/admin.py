from django.contrib import admin
from basket.models import Otlojit


class OtlojitAdmin(admin.ModelAdmin):
    fields = ['konkrnote', 'konkruser', 'zakaz']


admin.site.register(Otlojit, OtlojitAdmin)
