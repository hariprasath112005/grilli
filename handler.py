import os
import serverless_wsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()

def handler(event, context):
    return serverless_wsgi.handle_request(application, event, context)
