# Django Permalinks

This Django App acts as an internal redirector. Most likely use cases are when you have changed your URL scheme for a few pages, but your visitors still have the Old URL - this app can help you redirect the old scheme to the new one.

# Free URL Shortner

This Django app also provides a free URL shortner. In order to use it:
1. Use the Django Admin to make a new object of Permalinks.
2. While creating an object, you should see a link which says "Generate a random string". Click it.
3. Click the "Use this string" link when it appears.
4. Enter the long URL in the 'NEW URL' box above.

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
3. Add the permalinks URLs to `urls.py` of your base app **on the top of the list**:
     ```python
    urlpatterns = [
       url('', include('permalinks.urls')),
       ...
    ]
    ```

4. Add the permalinks middleware to `settings.py` **on the top of the list**:

    ```python
    MIDDLEWARE = [
       'permalinks.middleware.main.PermalinksMiddleware',
       ...
    ]
    ```

5. Run `manage.py migrate` to create the required table for the permalinks model.
6. Create your `permalinks` objects in your Django admin interface.
7. Test your OLD URLs and their responses by visiting them.
8. Enjoy a smooth URL migration!