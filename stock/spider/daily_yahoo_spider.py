#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/env/env python
# -*- coding: utf-8 -*-
from stock.spider.spider import Spider
import config.stock_config as stock_config
import urllib
import time
import json
import datetime
from datetime import date, datetime
from utils.yahoo_util import YahooUtil
import pytz
from utils.time_util import TimeUtli





class DailyYahooSpider(Spider):
    # TODO 可变参数的形式, 逻辑是如果指定了区间的话，按照指定的区间计算
    def __init__(self,stock, range = 60, interval = '1d',period_begin = None, period_end = None):
        Spider.__init__(self, stock)
        if period_begin and period_end:
            self.period_begin = period_begin
            self.period_end = period_end
        else:
            self.period_begin = int(time.time()) - range*86400
            self.period_end = int(time.time())
        self.interval = interval

    def generate_url(self):
        url_prefix = stock_config.YAHOO_DAILY_URL_PREFIX + self.stock + '?'
        params = {'period1': self.period_begin, 'period2':self.period_end, 'interval':self.interval}
        return url_prefix + urllib.urlencode(params)

    def parse_content_to_dict(self):
        content_json = self.get_content()
        #content_json = '{"chart":{"result":[{"meta":{"currency":"USD","symbol":"DATA","exchangeName":"NYQ","instrumentType":"EQUITY","firstTradeDate":1368777600,"gmtoffset":-14400,"timezone":"EDT","exchangeTimezoneName":"America/New_York","currentTradingPeriod":{"pre":{"timezone":"EDT","end":1500643800,"start":1500624000,"gmtoffset":-14400},"regular":{"timezone":"EDT","end":1500667200,"start":1500643800,"gmtoffset":-14400},"post":{"timezone":"EDT","end":1500681600,"start":1500667200,"gmtoffset":-14400}},"dataGranularity":"1d","validRanges":["1d","5d","1mo","3mo","6mo","1y","2y","5y","ytd","max"]},"timestamp":[1500643800],"indicators":{"quote":[{"high":[64.2699966430664],"close":[63.77000045776367],"volume":[382000],"open":[64.2699966430664],"low":[63.59000015258789]}],"unadjclose":[{"unadjclose":[63.77000045776367]}],"adjclose":[{"adjclose":[63.77000045776367]}]}}],"error":null}}'
        if(None == content_json) :
            return None
        content = json.loads(content_json)
        is_exist = YahooUtil.is_stock_result_exist(content_json)
        if is_exist is False:
            return None
        timestamp = content['chart']['result'][0]['timestamp']
        open = content['chart']['result'][0]['indicators']['quote'][0]['open']
        close = content['chart']['result'][0]['indicators']['quote'][0]['close']
        high = content['chart']['result'][0]['indicators']['quote'][0]['high']
        low = content['chart']['result'][0]['indicators']['quote'][0]['low']
        volume = content['chart']['result'][0]['indicators']['quote'][0]['volume']
        ret = []
        for i in range(0, len(timestamp)):
            temp = {}
            temp['date'] = TimeUtli.get_utc_date_from_timestamp(timestamp[i])
            temp['stock'] = self.stock
            temp['open'] =  open[i]
            temp['close'] = close[i]
            temp['high'] = high[i]
            temp['low'] = low[i]
            temp['volume'] = volume[i]
            ret.append(temp)
        return ret

if __name__ == '__main__':
    ins = MinuteYahooSpider('data',5)
    ret = ins.parse_content_to_dict()
    print ret
    #print ins.generate_url()
    timestamp = 1500667322-18000
    t1 = datetime.fromtimestamp(timestamp,pytz.timezone('UTC'))
    t1 = t1.date().__str__()
    print t1

    # ret = ins.parse_content_to_dict()
    # print ret


