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

Download and Install
====================

Download the source code:

::

  $ git clone git://github.com/macagua/django-local-flavor-ve.git

Install the source code adding the ``ve`` module to your ``PYTHONPATH`` environment variable:

::

  $ cd django-local-flavor-ve
  $ export PYTHONPATH=$PWD

On windows you may want to use ``set PYTHONPATH=%CD%``

Test your installation with the following commands from a Python shell:

::

  $ python
  >>> from ve import forms
  >>> dir(forms)
  >>> exit()

Cloned sources includes an example project. To try it out run:

::

  $ cd django-local-flavor-ve/example
  $ python manage.py runserver

Now that the server's running, visit http://127.0.0.1:8000/example/ with your Web browser. You'll see a "A Form example for Venezuelan localflavor" page. Then It worked!

Using Venezuela Local Flavor on my project
==========================================
You can see an example to use the Venezuelan Local Flavor in your Django_ projects here_.

Tested 
======

  * Django 1.2.4 and Python 2.6

TODO
====

  * Add full support to ISO-3166-2:VE_ regulations.
  * Write tests for all fields

.. _Django: http://djangoproject.com/
.. _localflavor: http://docs.djangoproject.com/en/dev/ref/contrib/localflavor/
.. _ISO-3166-2:VE: https://secure.wikimedia.org/wikipedia/en/wiki/ISO_3166-2:VE
.. _here: https://github.com/macagua/django-local-flavor-ve/tree/master/example

