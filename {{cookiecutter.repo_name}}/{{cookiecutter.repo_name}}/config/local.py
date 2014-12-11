# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
from configurations import values
from .common import Common


class Local(Common):

    # DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # Mail settings
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value(
        'django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + \
        ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += (
        'debug_toolbar',
        'django_extensions',  # Useful helper extensions
    )

    INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # end django-debug-toolbar

    # Django Extensions Configuration
    RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8080'
    # end Django Extensions Configuration.

    # Your local stuff: Below this line define 3rd party libary settings

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        ('postgres://{{cookiecutter.database_user}}:'
         '{{cookiecutter.database_password}}@'
         'localhost:5432/{{cookiecutter.database_name}}'
         )
    )
    # TEST DATABASE
    TEST = values.DatabaseURLValue(
        ('postgres://{{cookiecutter.database_user}}:'
         '{{cookiecutter.database_password}}@'
         'localhost:5432/test_{{cookiecutter.database_name}}'
         )
    )
    # END DATABASE CONFIGURATION
