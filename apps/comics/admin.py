from django.contrib import admin

from apps.comics.models import Comic, Page, TagType, Tag

admin.site.register(Comic)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(TagType)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('type',)
