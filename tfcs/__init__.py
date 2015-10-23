#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tanky Woo @ 2015-10-18
import os
import yaml
from flask import Flask

app = Flask(__name__)
app.config.from_object('configs')

base_dir = os.path.dirname(os.path.dirname(__file__))
site_cfg = yaml.load(open(os.path.join(base_dir, 'site.yaml'), 'r'))

from tfcs import views
