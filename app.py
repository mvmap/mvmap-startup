#!/usr/bin/env python

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import torndb
from tornado.options import define, options

from settings import *

from urls import url_patterns as handlers
from handlers.uimodules import *

define("port", default=8008, help="run on the given port", type=int)


settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    ui_modules=[{'Company': CompanyModule}, {'Page': PageModule}],
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    debug=True,
)


class Application(tornado.web.Application):

    def __init__(self):
        self.db = db
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
