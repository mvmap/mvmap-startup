#!/usr/bin/env python

from handlers.home import HomeHandler

url_patterns = [
    (r"/", HomeHandler),
]
