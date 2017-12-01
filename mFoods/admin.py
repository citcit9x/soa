from django.contrib import admin
from .models import Foods

class FoodsAdmin(admin.ModelAdmin):
    list_display = ["id","content_text", "get_photo", "create_date"]
    list_filter = ["create_date" ]

    def get_photo(self, obj):
        return ('<img src="{photo}" alt="" width="100"/>').format(
            photo=obj.url_img,
        )
    get_photo.allow_tags = True
    get_photo.short_description = 'Preview'

admin.site.register(Foods, FoodsAdmin)
admin.site.site_header = 'Admin Foods - Dịch Vụ'
admin.site.index_title = 'DataBase Foods Center'
