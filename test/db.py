#!/usr/bin/env python
# encoding:utf-8
import MySQLdb as mdb
import torndb

conn = mdb.connect("localhost", "root", "root", "startups")

tdb = torndb.Connection("localhost", "startups", "root", "root")


def getCompanyInfo():
    with conn:
        cur = conn.cursor()
        cur.execute("select * from company limit 2")
        all = cur.fetchall()
        print type(all)
        print all
        # for i in range(cur.rowcount):
        #     row = cur.fetchone()
        #     print type(row)
        #     print row


def tdb_test():
    # res = tdb.query("select status, domain, tags from company limit 2")
    res = tdb.query("select count(id) as total from company")
    print type(res)
    for c in res:
        # print type(c)
        # print c.status, c.domain, c.tags
        print c.total

if __name__ == '__main__':
    # getCompanyInfo()
    tdb_test()
