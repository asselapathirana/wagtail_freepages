from django.db import models

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

from demo.models import CarouselItem, RelatedLink

from wagtail.wagtailsearch import index
# Standard page Free Form

class StandardPageFreeFormCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('freepages.StandardPageFreeForm', related_name='carousel_items')


class StandardPageFreeFormRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('freepages.StandardPageFreeForm', related_name='related_links')


class StandardPageFreeForm(Page):
    intro = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ],null=True,blank=True)
    
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro',partial_match=True),
        index.SearchField('body'),
    )

StandardPageFreeForm.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel(StandardPageFreeForm, 'carousel_items', label="Carousel items"),
    StreamFieldPanel('body'),
    InlinePanel(StandardPageFreeForm, 'related_links', label="Related links"),
]

StandardPageFreeForm.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]



