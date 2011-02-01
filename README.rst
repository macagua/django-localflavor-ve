=================================
Django Local Flavor For Venezuela
=================================

A django_ localflavor_ For Venezuela.

- Code repository: http://github.com/macagua/django-local-flavor-ve
- Questions and comments to http://github.com/macagua/django-local-flavor-ve/issues
- Report bugs at http://github.com/macagua/django-local-flavor-ve/issues


.. contents::

Features
========

More than a long speech, here the list of the main features :

  * A field that accepts a 'classic' NNNN Zip Zone Code.
  * A field that validates 'Cédula de Identidad' (DNI) numbers.
  * A field that validates a Register Tax Information (Registro Único de Información Fiscal - RIF) issued by SENIAT.
  * A field that validates as Venezuelan phone postal code.
  * A Select widget that uses a list of Venezuelan regions as its choices.
  * A Select widget that uses a list of Venezuelan states as its choices.
  * A Select widget that uses a list of Venezuelan municipalities as its choices.

Tested 
======

  * Django 1.1.1 and Python 5


TODO
====

  * Add suport for the Django last version 
  * Define on based ISO 3166-2:VE the code for regions,states, municipalities and parishes.
  * A Select widget that uses a list of Venezuelan municipalities as its choices.
  * A Select widget that uses a list of Venezuelan parishes as its choices.


.. _django: http://djangoproject.com/
.. _localflavor: http://docs.djangoproject.com/en/dev/ref/contrib/localflavor/
  

