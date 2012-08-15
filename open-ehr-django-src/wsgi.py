import os
import sys
sys.path.insert(0,"/media/data/Project/open-ehr")
sys.path.append("/media/data/Project/open-ehr")

os.environ['DJANGO_SETTINGS_MODULE'] = 'open-ehr.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
