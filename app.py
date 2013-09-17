#!/usr/bin/env python

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from urls import url_patterns as handlers

define("port", default=8888, help="run on the given port", type=int)


settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    debug=True,
)


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
