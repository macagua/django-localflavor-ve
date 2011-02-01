# -*- coding: utf-8 -*-
"""
An alphabetical list of Venezuelan municipalities for use as 'choices'
in a formfield.

This exists in this standalone file so that it's on ly imported into memory
when explicitly needed.

Data based Excel file from INE http://www.ine.gob.ve/venezuelaenmapas/mapasvenezuela.asp
"""

MUNICIPALITIES_CHOICES = (
    ('140100', _(u'Alberto Adriani'), 'VE-L'),
    ('140200', _(u'Andrés Bello'), 'VE-L'),
    ('140300', _(u'Antonio Pinto Salinas'), 'VE-L'),
    ('140400', _(u'Aricagua'), 'VE-L'),
    ('140500', _(u'Arzobispo Chacón'), 'VE-L'),
    ('140600', _(u'Campo Elías'), 'VE-L'),
    ('140700', _(u'Caracciolo Parra Olmedo'), 'VE-L'),
    ('140800', _(u'Cardenal Quintero'), 'VE-L'),
    ('140900', _(u'Guaraque'), 'VE-L'),
    ('141000', _(u'Julio César Salas'), 'VE-L'),
    ('141100', _(u'Justo Briceño'), 'VE-L'),
    ('141200', _(u'Libertador'), 'VE-L'),
    ('141300', _(u'Miranda'), 'VE-L'),
    ('141400', _(u'Obispo Ramos de Lora'), 'VE-L'),
    ('141500', _(u'Padre Noguera'), 'VE-L'),
    ('141600', _(u'Pueblo Llano'), 'VE-L'),
    ('141700', _(u'Rangel'), 'VE-L'),
    ('141800', _(u'Rivas Dávila'), 'VE-L'),
    ('141900', _(u'Santos Marquina'), 'VE-L'),
    ('142000', _(u'Sucre'), 'VE-L'),
    ('142100', _(u'Tovar'), 'VE-L'),
    ('142200', _(u'Tulio Febres Cordero'), 'VE-L'),
    ('142300', _(u'Zea'), 'VE-L'),
)
