"""
WSGI config for app_vigas project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_vigas.settings')

application = get_wsgi_application()

# Vercel handler
app = application