from django.contrib import admin
from .models import UpcommingDivePost


class PropertyImageInline(admin.TabularInline):
    model = UpcommingDivePost
    extra = 3


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, ]


admin.site.register(UpcommingDivePost, PropertyAdmin)
