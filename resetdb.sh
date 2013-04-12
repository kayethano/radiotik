#!/bin/sh

sudo -u postgres dropdb radiotik
sudo -u postgres createdb radiotik
python manage.py syncdb --settings radiotik.localsettings
python manage.py runserver --settings radiotik.localsettings
