#!/usr/bin/env python

from base import BaseHandler


class HomeHandler(BaseHandler):

    def get(self):
        self.write("This is home page!")
