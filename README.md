# Django Permalinks

This Django App makes sures that all your old URLs work in case you have migrated your old Primary Key URL slugs, or for whatever reason your data for the views are inconsistent.

# Installation

Install from PyPI:
```terminal
pip install django-permalinks
```

# Configurations

1. Add `permalinks` to your list of `INSTALLED_APPS` in settings.py:

    ```python
    INSTALLED_APPS = [
        ...
        'permalinks',
        ...
    ]
    ```

 2. Add the permalinks web app URLs to urls.py **on the top of the list**:

    ```python
    from django.urls import url, include
    
    urlpatterns = [
        # Make sure permalinks.url is FIRST in the URLs array.
        url('', include('permalinks.urls')),  # You MUST use an empty string as the URL prefix
        ...
    ]
    ```

3. Run `manage.py migrate` to create the required table for the permalinks model.
4. Create your `permalinks` objects in your Django admin interface.
5. Test your OLD URLs and their responses by visiting them.
6. Enjoy a smooth URL migration!