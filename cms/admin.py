from django.contrib import admin
from .models import SliderCms
from django.utils.safestring import mark_safe
# Register your models here.
class CMSAdmin(admin.ModelAdmin):
    list_display = ('slider_title', 'slider_desr','slider_css','get_img')
    list_display_links = ('slider_title',)
    list_editable = ('slider_css',)
    fields = ('slider_title', 'slider_desr','slider_css','slider_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.slider_img:
            return mark_safe(f'<img src="{obj.slider_img.url}" width="80px" height="80px" >')
        else:
            return 'нет картинки'
    get_img.short_description = 'Миниатюра'

admin.site.register(SliderCms, CMSAdmin)