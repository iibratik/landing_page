from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm
# Register your models here.
class Comment(admin.StackedInline):
    model = ComentCrm
    fields = ('comment_text', 'comment_dt',)
    readonly_fields = ('comment_dt',)
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_created')
    list_display_links = ('id', 'order_name',)
    search_fields = ('id', 'order_name', 'order_phone', 'order_created')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_created', 'order_status' , 'order_name' ,'order_phone')
    readonly_fields = ('id', 'order_created',)
    # Поле класса Comment
    inlines = [Comment,]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)