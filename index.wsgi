import sae
from Bidding import wsgi
application = sae.create_wsgi_app(wsgi.application)