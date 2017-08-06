# -*- coding: utf-8 -*-
import stock.spider.spider as sina_spider
import config.stock_config as stock_config
import urllib
import time

class MinuteSinaSpider(sina_spider.SinaSpider):


    def generate_url(self):
        url_prefix = stock_config.SINA_MINUTE_URL_PREFIX
        params = {'symbol': self.stock, 'random':time.time()*100,'day':5}
        return url_prefix + urllib.urlencode(params)
    @staticmethod
    def get_colprefix_by_minute(minute):
        return minute[0:5]

    def parse_content_to_dict(self):
        content = self.get_content()
        # 去掉多余的字符串
        content = content.replace('data=((new String(" ', '').replace('")));','')
        daily_list = content.split(' ')
        all_rows_data = []
        for one_day in daily_list:
            one_row_data = {}
            date = one_day[0:10]
            one_row_data['date'] = date
            one_day = one_day[11:]
            one_day_list = one_day.split(';')

            for one_minute in one_day_list:
                col_prefix = MinuteSinaSpider.get_colprefix_by_minute(one_minute)

                col_volume_name = col_prefix + '_volume'
                col_price_name = col_prefix + '_price'

                minute_list = one_minute.split(',')
                one_row_data[col_volume_name] = minute_list[1]
                one_row_data[col_price_name] = minute_list[3]
            all_rows_data.append(one_row_data)
if __name__ == "__main__":
    ins = MinuteSinaSpider('baba')
    ins.parse_content_to_dict()
    for i in range(9,16):
        for j in range(0,60):
            if j < 10:
                print 'volume_' +str(i)+'_0'+str(j) + ' = Column(Integer)'
                print 'low_' + str(i)+'_0'+str(j) + '_low = Column(Float)'
                print 'high_' + str(i)+'_0'+str(j) + ' = Column(Float)'
                print 'open_' + str(i) + '_0' + str(j) + ' = Column(Float)'
                print 'close_' + str(i) + '_0' + str(j) + ' = Column(Float)'

            else:
                print 'volume_' + str(i)+'_'+str(j) + ' = Column(Integer)'
                print 'low_' + str(i)+'_'+str(j) + ' = Column(Float)'
                print 'high_' + str(i)+'_'+str(j) + ' = Column(Float)'
                print 'open_'+ str(i) + '_' + str(j) + ' = Column(Float)'
                print 'close_' + str(i) + '_' + str(j) + ' = Column(Float)'


