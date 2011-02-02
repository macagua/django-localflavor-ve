=================================
Django Local Flavor For Venezuela
=================================

A Django_ localflavor_ For Venezuela.

- Code repository: http://github.com/macagua/django-local-flavor-ve
- Questions, comments and bug reports to http://github.com/macagua/django-local-flavor-ve/issues

.. contents::

Features
========

  * A field that accepts a 'classic' NNNN Zip Zone Code.
  * A field that validates 'Cédula de Identidad' (DNI) numbers.
  * A field that validates a Register Tax Information (Registro Único de Información Fiscal - RIF) issued by SENIAT.
  * A field that validates as Venezuelan phone postal code.
  * A Select widget that uses a list of Venezuelan regions as its choices.
  * A Select widget that uses a list of Venezuelan states as its choices.

Tested 
======

  * Django 1.2.4 and Python 2.6

TODO
====

  * Add suport for the Django latest version 
  * Implement fields for regions, states, municipalities and parishes based on ISO-3166-2:VE_ regulations.
  * Add examples to use the Venezuelan Local Flavor

.. _Django: http://djangoproject.com/
.. _localflavor: http://docs.djangoproject.com/en/dev/ref/contrib/localflavor/
.. _ISO-3166-2:VE: https://secure.wikimedia.org/wikipedia/en/wiki/ISO_3166-2:VE

