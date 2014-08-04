from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged, SiteRelated
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
    '''
    NOT USED
    '''

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class IndexPage(Page, RichText):
    '''
    A page representing the format of the home/hem/index page
    '''

    image_left = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.HomePage.image", "feature_image"),
        format="Image", max_length=255, null=True, blank=True)
    image_right = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.HomePage.image", "feature_image"),
        format="Image", max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = _("Index page")
        verbose_name_plural = _("Index pages")
      

class SitewideContent(SiteRelated):
    '''
    Represents the footer content
    '''
    box_one_content = RichTextField()


    class Meta:
        verbose_name = _('Sitewide Content')
        verbose_name_plural = _('Sitewide Content')
