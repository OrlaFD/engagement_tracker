# engagement_tracker

During the project set up…

pip install django

For boilerplate files: 
django-admin startproject engagement_tracker 

Then created an application (‘base’) to break down the project (‘engagement_tracker’) into manageable components: 
python manage.py startapp base

connect project to application (two don’t know about each other) via settings.py (engagement_tracker) by adding ‘base.apps.BaseConfig’ under INSTALLED_APPS
 

Created a urls.py file 
Connect Views and URLs files to allow for URL routing (url patterns)
