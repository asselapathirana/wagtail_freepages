# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import wagtail.wagtailcore.fields
import django.db.models.deletion
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailimages', '0006_add_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPageFreeForm',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='wagtailcore.Page', serialize=False)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), null=True, blank=True)),
                ('feed_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StandardPageFreeFormCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(related_name='carousel_items', to='freepages.StandardPageFreeForm')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StandardPageFreeFormRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_document', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(null=True, related_name='+', blank=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='freepages.StandardPageFreeForm')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
    ]
