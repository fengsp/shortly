"""
    shortly.views
    ~~~~~~~~~~~~~

    Register actions.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
from flask import request, abort, redirect
from flask import render_template

from shortly import app
from shortly.utils import is_valid_url, base52_encode
from shortly.models import db


def shorten(url):
    """Simple shorten logic.
    `original-short` + url will store the short id.
    `short-original` + short_id will store the corresponding original url.

    :param url: The original url you want to shorten.
    """
    short_id = db.get('original-short:' + url)
    if short_id is not None:
        return short_id
    num = db.incr('url-autoincr-id')
    short_id = base52_encode(num)
    db.set('original-short:' + url, short_id)
    db.set('short-original:' + short_id, url)
    return short_id


@app.route('/', methods=['GET', 'POST'])
def shortly():
    error = None
    url = ''
    shortly_count = db.get('shortly-count') or '0'
    if request.method == 'POST':
        url = request.form['url']
        if not is_valid_url(url):
            error = 'Invalid URL'
        else:
            short_id = shorten(url)
            return short_id
    return render_template('shortly.html', error=error, url=url, 
                                           shortly_count=shortly_count)


@app.route('/<short_id>')
def original(short_id):
    original_url = db.get('short-original:' + short_id)
    if original_url is None:
        abort(404)
    db.incr('shortly-count')
    return redirect(original_url)
