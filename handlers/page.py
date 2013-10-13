from base import BaseHandler
from pagination import Paginator

class PageHandler(BaseHandler):

    def get(self, page):
        pager = Paginator(self.db)
        if int(page) > pager.pages:
            pager.page = pager.pages
        elif int(page) < 1:
            pager.page = 1
        else:
            pager.page = int(page)
        com = pager.get_company()
        self.render(
            "home.html", companies=com, paginator=pager)
