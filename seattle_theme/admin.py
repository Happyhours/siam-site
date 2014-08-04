from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import SingletonAdmin


# Register your models here.
from seattle_theme.models import (
    HomePage,
    IndexPage,
    SitewideContent,
)

#class HomePageAdmin(PageAdmin):
#    pass

#admin.site.register(HomePage, HomePageAdmin)


class IndexPageAdmin(PageAdmin):
    pass

admin.site.register(IndexPage, IndexPageAdmin)


class SitewideContentAdmin(SingletonAdmin):
   pass

admin.site.register(SitewideContent, SitewideContentAdmin)

# class ContactMapInline(TabularDynamicInlineAdmin):
#     model = ContactMap
#
#
# class ContactPageAdmin(PageAdmin):
#     inlines = [ContactMapInline]
#
#
# admin.site.register(ContactPage, ContactPageAdmin)
