import os
import sys
import serverless_wsgi
from django.core.wsgi import get_wsgi_application

# Add the project root to the python path
# When running as a Netlify function, the root of the repo is usually two levels up from this file
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, root_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()

def handler(event, context):
    return serverless_wsgi.handle_request(application, event, context)
