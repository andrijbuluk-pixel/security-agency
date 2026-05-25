# Security Agency Project



1. Preparation of the database
First, you need to apply migrations to create a table structure in your database:
`python manage.py migrate`.

##
2. Downloading test data
If you have an initial data file, upload it so you don't start with a completely empty project:
`python manage.py loaddata initial-date.json`.

##
3. Creating an administrator
Create a superuser account to access the administration panel:
`python manage.py createsuperuser`.





