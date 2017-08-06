#!/usr/env/env python
# -*- coding: utf-8 -*-
from utils.urllib_tool import UrllibTool
from bs4 import BeautifulSoup
class stockInfoSpider:
    @staticmethod
    def get_all_stock_symbol():
        pass


    @staticmethod
    def get_one_page_stock_list(page = 1, pagesize =200):
        url = '''http://www.nasdaq.com/g00/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=200&page='''+ str(i)
        s = UrllibTool.get_page_content(url)
        soup = BeautifulSoup(s, "html.parser")
        ret =soup.find(id="CompanylistResults").find_all('h3')

        stock_list = []
        for one in ret:
            link = one.find('a').text
            symbol = ''.join(link.split())
            stock_list.append(symbol)
        return stock_list
