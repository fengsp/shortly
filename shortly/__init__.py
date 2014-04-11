"""
    shortly.app
    ~~~~~~~~~~~

    Shortly app inspired by http://werkzeug.pocoo.org/docs/tutorial/.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
from flask import Flask
app = Flask(__name__)
from shortly import settings
app.config.from_object(settings)

import shortly.views
