"""
    shortly.app
    ~~~~~~~~~~~

    Shortly app.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
from flask import Flask
app = Flask(__name__)
from shortly import settings
app.config.from_object(settings)

import shortly.views
