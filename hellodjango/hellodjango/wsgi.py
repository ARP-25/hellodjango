"""
WSGI config for hellodjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hellodjango.settings')

os.environ.setdefault("DATABASE_URL", "postgres://rrpwhrdm:hEUS3hF_n71r_y8t_3jEqGzlOyZATWtD@trumpet.db.elephantsql.com/rrpwhrdm")



application = get_wsgi_application()
