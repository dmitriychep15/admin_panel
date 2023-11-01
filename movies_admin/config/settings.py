"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""


from dotenv import load_dotenv
from split_settings.tools import include


load_dotenv()


include(
    'components/database.py',
    'components/internationalization.py',
    'components/app_definition.py',
    'components/auth.py',
    'components/development.py',
    'components/paths.py',
)
