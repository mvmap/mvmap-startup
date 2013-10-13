#!/usr/bin/env python

from handlers.home import HomeHandler
from handlers.page import PageHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/page/([0-9]+)", PageHandler),
]
