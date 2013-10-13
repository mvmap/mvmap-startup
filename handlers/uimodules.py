__all__ = ["CompanyModule", "PageModule"]
import tornado.web


class CompanyModule(tornado.web.UIModule):

    def render(self, company):
        return self.render_string("modules/company.html", company=company)


class PageModule(tornado.web.UIModule):

    def render(self, paginator):
        return self.render_string("modules/pagination.html", paginator=paginator)
