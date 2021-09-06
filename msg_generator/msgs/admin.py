from django.contrib import admin

from .models import MsgForm, Message


class MsgFormAdmin(admin.ModelAdmin):
    list_filter = ['variables_quantity', 'pub_date']
    search_fields = ['template_text']
    ordering = ('-variables_quantity',)
    list_display = ('template_text', 'pub_date', 'variables_quantity')
    fieldsets = [
        (None,               {'fields': ['template_text', 'variables_quantity']}),

        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


admin.site.register(MsgForm, MsgFormAdmin)
admin.site.register(Message)

