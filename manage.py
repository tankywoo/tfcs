#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Server
from tfcs import app

manager = Manager(app)

manager.add_command('runserver', Server(use_debugger=True))


if __name__ == '__main__':
    manager.run()
