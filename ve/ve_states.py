# -*- coding: utf-8 -*-
"""
A list of Venezuelan states for use as `choices` in a formfield.

This exists in this standalone file so that it's only imported into memory
when explicitly needed.

Data based from ISO_3166-2:VE http://en.wikipedia.org/wiki/ISO_3166-2:VE
"""

from django.utils.translation import ugettext_lazy as _

STATE_CHOICES = (
    ('VE-X', _(u'Amazonas')),
    ('VE-B', _(u'Anzoátegui')),
    ('VE-C', _(u'Apure')),
    ('VE-D', _(u'Aragua')),
    ('VE-E', _(u'Barinas')),
    ('VE-F', _(u'Bolívar')),
    ('VE-G', _(u'Carabobo')),
    ('VE-H', _(u'Cojedes')),
    ('VE-Y', _(u'Delta Amacuro')),
    ('VE-Z', _(u'Dependencias Federales')),
    ('VE-A', _(u'Distrito Capital')),
    ('VE-I', _(u'Falcón')),
    ('VE-J', _(u'Guárico')),
    ('VE-K', _(u'Lara')),
    ('VE-L', _(u'Mérida')),
    ('VE-M', _(u'Miranda')),
    ('VE-N', _(u'Monagas')),
    ('VE-O', _(u'Nueva Esparta')),
    ('VE-P', _(u'Portuguesa')),
    ('VE-R', _(u'Sucre')),
    ('VE-S', _(u'Táchira')),
    ('VE-T', _(u'Trujillo')),
    ('VE-W', _(u'Vargas')),
    ('VE-U', _(u'Yaracuy')),
    ('VE-V', _(u'Zulia')),
)

