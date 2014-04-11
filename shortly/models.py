# -*- coding: utf-8 -*-
"""
    shortly.models
    ~~~~~~~~~~~~~~

    Shortly db.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""

from redis import Redis

from shortly import app


db = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], 
           db=app.config['REDIS_DB'])
