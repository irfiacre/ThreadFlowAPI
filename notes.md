## Some things I learned.

Issue1. I deleted my postgres tables, and wanted to create them again using:

###### Approach:
- Delete Migration Files `find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`
- Log in to your PostgreSQL database and delete entries from the django_migrations table using `DELETE FROM django_migrations;`
- Then:
```
    python manage.py makemigrations
    python manage.py migrate
```
