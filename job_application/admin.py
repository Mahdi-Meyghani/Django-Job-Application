from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name")
    list_filter = ("date", "occupation")
    ordering = ("date", )
    readonly_fields = ("date", )


admin.site.register(Form, FormAdmin)

