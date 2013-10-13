# encoding:utf-8

from base import BaseHandler
from pagination import Paginator


class HomeHandler(BaseHandler):

    def get(self):
        pager = Paginator(self.db, 1)
        # self.write("It's ok")
        com = pager.get_company()
        self.render(
            "home.html", companies=com, paginator=pager)

