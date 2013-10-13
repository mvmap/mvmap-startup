#!/usr/bin/env python
# encoding:utf-8

import urllib
from bs4 import BeautifulSoup
# internet
# list_url = "http://itjuzi.com/company?scope=1&page="
# software
list_url = "http://itjuzi.com/company?scope=10&page="
cmp_fmt = 'insert into company(company_name,product_name, website, location, \
            create_time, status, stage, domain, tags, intro, thumb_large, thumb_small,juzi_url) \
            values("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}", "{11}","{12}");\n'
sql_fmt1 = 'insert into company(company_name,product_name, website, location, \
            create_time, status, stage, domain, tags, intro, thumb_large, thumb_small,juzi_url) \
            values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s","%s");\n'
produc_fmt = 'insert into products(company_id, product_name, product_type, product_url, product_intro, juzi_url)\
            values(%d,"%s","%s","%s","%s", "%s");\n'


def getCompanyList():
    try:
        com_file = open("company-2.sql", "w")
        prod_file = open("products-2.sql", "w")
    except Exception, e:
        print e
    count = 916
    for i in range(1, 10):
        html = urllib.urlopen(list_url + str(i)).read()
        bs = BeautifulSoup(html)
        # companies = bs.find_all("div", class="company-list-item")
        companies = bs.find_all("div", attrs={"class": "company-list-item"})
        for cmp in companies:
            count += 1
            cmp_detail_url = cmp.find(attrs={"class": "media-tit"}).get("href")
            thumb_s = cmp.find(attrs={"class": "media-object"}).get("src")
            # print type(thumb_s)
            # print cmp_detail_url, thumb_s
            detail_html = urllib.urlopen(cmp_detail_url).read().decode("utf-8")
            detail = BeautifulSoup(detail_html)

            product = detail.find(attrs={"id": "com_id_value"}).get_text()
            thumb_l = detail.find(attrs={"id": "company_big_show"}).get("src")
            # print type(product), type(thumb_l)
            basic_info = detail.find(
                "ul", attrs={"class": "detail-info"}).find_all("li")
            company_url = basic_info[0].find("a").get("href")
            # print type(company_url)
            company_name = basic_info[1].find("em").get_text()
            # print type(company_name)
            company_create_time = basic_info[2].find("em").get_text()
            province = basic_info[3].find(
                "a").get_text() if basic_info[3].find("a") else ""
            # print type(province)
            city = basic_info[3].find(
                "em").get_text() if basic_info[3].find("em") else ""
            company_location = province + city
            company_status = basic_info[4].find("a").get_text()
            company_stage = basic_info[5].find("a").get_text()
            company_domain = basic_info[6].find("a").get_text()
            tags = basic_info[7].find_all("a")
            company_tags = []
            for t in tags:
                company_tags.append(t.get_text())

            company_intro = basic_info[8].find("em").get_text()

            products = detail.find_all(
                "div", attrs={"class": "company-product-item"})
            company_products = []
            for pr in products:
                a = pr.find_all("a")
                href = a[0].get("href").encode('utf-8')
                name = a[0].get_text().encode("utf-8")
                p_type = a[1].get_text().encode("utf-8")
                p = pr.find("p").get_text().encode("utf-8")
                company_products.append([name, p_type, href, p])
            for l in company_products:
                pro = produc_fmt % (
                    count, l[0], l[1], l[2], l[3], cmp_detail_url)
                prod_file.write(pro)

            # out = sql_fmt %(str(company_name), str(product), str(company_url), str(company_location), str(company_create_time), \
            #         str(company_status), str(company_stage), str(company_domain), str(",".join(company_tags)), str(company_intro), \
            #         str(thumb_l),str(thumb_s), str(cmp_detail_url))

            out = cmp_fmt.format(
                company_name.encode("utf-8"), product.encode("utf-8"), company_url, company_location.encode(
                    "utf-8"), company_create_time.encode("utf-8"),
                company_status.encode("utf-8"), company_stage.encode("utf-8"), company_domain.encode(
                    "utf-8"), ",".join(company_tags).encode("utf-8"), company_intro.encode("utf-8"),
                thumb_l, thumb_s, cmp_detail_url)
            com_file.write(out)
            # print company_name
            # print company_tags
            # print [cmp_detail_url, company, company_name, company_url, company_create_time,\
            #         company_location, company_status, company_stage, company_domain, company_tags,\
            #         company_intro, company_products, thumb_s,thumb_l]
    com_file.close()
    prod_file.close()


def has_no_class_no_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")


if __name__ == '__main__':
    # main()
    getCompanyList()
