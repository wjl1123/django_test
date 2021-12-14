"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
>>>>>>> cb7e79f78658e358f32333a62d168513d0948493
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
