from django.contrib import admin
from .models import login,add,borrow


class BooksAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields": ["book_name"]}),
        ("More information",{"fields":["auther_name","type_book","details","image"]}),
    ]

    list_display = ["book_name","type_book","auther_name"]
    list_filter = ["type_book"]
    search_fields = ["book_name","type_book"]
    list_per_page = 10

# Register your models here.
#
admin.site.register(login)
admin.site.register(add,BooksAdmin)
admin.site.register(borrow)