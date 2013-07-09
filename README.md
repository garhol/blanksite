blanksite
=========

Blank django/bootstrap site

Blank site and starting point for small projects.
Basic setup with bootstrap in place and local_settings.

Sample view in lib/apps/home to prevent "congratulations" page.


Setup:

* Setup a new blank django app (copy the secret key for easiness)
* Checkout over the top of the django app and then set up your static application (nginx or similar)
* Link your library folders to the root of your static folder ('ln -s /home/site/garhol/library/css /home/staticsite')
* Setup a new SECRET_KEY in lib/settings.py (or steal from the application you have overwritten)
* Set your local_settings to point at the static root and media root.
* Add your apps in lib/apps either using 'manage.py startapp appname' or by copying and pasting the home app.
* Remember to add a requirements.txt in the root which can be generated from pip freeze

