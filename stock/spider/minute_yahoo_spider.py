#!/usr/env/env python
# -*- coding: utf-8 -*-
from stock.spider.spider import Spider
import config.stock_config as stock_config
import urllib
import time
import json
import datetime
from utils.urllib_tool import UrllibTool
from bs4 import BeautifulSoup
from utils.yahoo_util import YahooUtil


class MinuteYahooSpider(Spider):
    def __init__(self,stock, range = '1d', interval = '1m'):
        Spider.__init__(self, stock)
        self.range = range
        self.interval = interval

    def generate_url(self):
        url_prefix = stock_config.YAHOO_MINUTE_URL_PREFIX + self.stock + '?'
        params = {'range': self.range, 'interval':self.interval}
        return url_prefix + urllib.urlencode(params)

    def parse_content_to_dict(self):
        content_json = self.get_content()
        if None == content_json:
            return None
        content = json.loads(content_json)

        is_exist = YahooUtil.is_stock_result_exist(content_json)
        if is_exist is False:
            return None
        time = json.dumps(content['chart']['result'][0]['timestamp'])
        open = json.dumps(content['chart']['result'][0]['indicators']['quote'][0]['open'])
        close = json.dumps(content['chart']['result'][0]['indicators']['quote'][0]['close'])
        high = json.dumps(content['chart']['result'][0]['indicators']['quote'][0]['high'])
        low = json.dumps(content['chart']['result'][0]['indicators']['quote'][0]['low'])
        volume = json.dumps(content['chart']['result'][0]['indicators']['quote'][0]['volume'])
        timestamp = content['chart']['result'][0]['meta']['currentTradingPeriod']['regular']['start']
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        return {
            'date':date,
            'stock':self.stock,
            'time':time,
            'open':open,
            'close':close,
            'high':high,
            'low':low,
            'volume':volume
        }
if __name__ == '__main__':

    # ins = MinuteYahooSpider('data')
    # print ins.generate_url()
    # ret = ins.parse_content_to_dict()
    # print ret
    for i in range(17,18):
        url = '''http://www.nasdaq.com/g00/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=200&page='''+ str(i)
        s = UrllibTool.get_page_content(url)
        soup = BeautifulSoup(s, "html.parser")
        ret =soup.find(id="CompanylistResults").find_all('h3')

        for one in ret:
            link = one.find('a').text
            symbol = ''.join(link.split())
            print symbol
        print "\n"
