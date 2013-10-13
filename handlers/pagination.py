#!/usr/bin/env python
# encoding:utf-8
from math import ceil


class Paginator(object):

    def __init__(self, db, page=1, per_page=10):
        #: pagination object.
        self.db = db
        self.total = self.get_total()
        #: the current page number (1 indexed)
        self.page = page
        #: the number of items to be displayed on a page.
        self.per_page = per_page

    @property
    def pages(self):
        """The total number of pages"""
        return int(ceil(self.total / float(self.per_page)))

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    def get_total(self):
        # return 55
        return self.db.query("select count(id) as total from company")[0].total

    def get_company(self):
        data = self.db.query("select company_name,product_name, website, \
            location, create_time, status, stage, domain, tags, thumb_small,\
            intro from company limit %s, %s" , (self.page - 1), 10)
        return data
