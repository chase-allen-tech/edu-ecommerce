
import logging
from django.apps import apps
from django.conf.urls import include, url

payment = apps.get_app_config('payment')
application = apps.get_app_config('ecommerce')

logging.info("[logging info]")
logging.info(application.urls[0])

urlpatterns = [
    url(r'^api/', include(('ecommerce.extensions.api.urls', 'api'))),
    url(r'^payment/', include(payment.urls[0])),
    url(r'', include(application.urls[0])),
]
