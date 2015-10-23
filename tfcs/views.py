#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tanky Woo @ 2015-10-18
import os
import re
import yaml
import markdown
from flask import url_for, session, render_template, abort
from tfcs import app
from tfcs import site_cfg


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', site=site_cfg), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', site=site_cfg), 500


def parse_markup(markup_text):
    markdown_extensions = [
        'fenced_code',
        'extra',
        'codehilite(css_class=hlcode)',
    ]

    _html = markdown.markdown(
        markup_text,
        extensions=markdown_extensions
    )

    return _html


def get_snippets(with_body=False):
    regex = re.compile('(?sm)^---(?P<meta>.*?)^---(?P<body>.*)')
    snippets_l = []
    for root, dirs, files in os.walk(app.config['SNIPPETS_ROOT']):
        files = [f for f in files if not f.startswith(".")]
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fn in files:
            if not fn.endswith('.md'):
                continue
            _fd = open(os.path.join(root, fn), 'r')
            _match_obj = re.match(regex, _fd.read())
            if _match_obj:
                _data = yaml.load(_match_obj.group('meta'))
                # pure digit in yaml is int
                _data['id'] = str(_data['id'])
                if _data.get('tag'):
                    _data.update({'tag': _data['tag'].split(',')})
                _data['category'] = os.path.split(root)[1]
                if with_body:
                    _html_body = parse_markup(
                        unicode(_match_obj.group('body'), 'utf-8') # xxx
                    )
                    _data['body'] = _html_body
                snippets_l.append(_data)

    # sort by datetime
    snippets_l = sorted(snippets_l, key=lambda m: m['date'], reverse=True)

    return snippets_l


@app.route('/')
def index():
    snippets_l = get_snippets()
    return render_template('index.html', snippets_l=snippets_l, site=site_cfg)


@app.route('/<url_id>/')
def post(url_id):
    snippets_l = get_snippets(True)
    snippet = None
    for s in snippets_l:
        # xxx: url_id is unicode, and s['id'] is str
        if s['id'] == url_id:
            snippet = s
            break
    else:
        abort(404)

    return render_template('post.html', snippet=snippet, site=site_cfg)
