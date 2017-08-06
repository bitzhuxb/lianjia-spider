# -*- coding: utf-8 -*-

import re
import urllib2
import random
import threading
import logging
from bs4 import BeautifulSoup
from model.lj_district import LjDistrict
from time import sleep
import time
from utils.urllib_tool import UrllibTool


import sys
reload(sys) #疑问
sys.setdefaultencoding("utf8")
sys.path.append("..")
import config.config
hds = config.config.hds
class DistrictSpider(object):
    def __init__(self,city):
        self.city = city
        self.plain_text = None
    def get_url(self):
        return u'http://'+ self.city + '.lianjia.com/chengjiao/'
    def get_page_content(self):
        print self.get_url()
        return UrllibTool.get_page_content(self.get_url())
    def parse_districts(self):
        self.plain_text = self.get_page_content()
        print self.plain_text
        soup = BeautifulSoup(self.plain_text, "html.parser")
        district_soup_list = soup.find('div', {'data-role': 'ershoufang'}).find_all('a')
        district_list = {}
        for district in district_soup_list:
            district_id = district.attrs['href'].replace('/chengjiao/','').replace('/','')
            district_name = district.text
            district_list[district_id] = district_name
        return district_list
    def save_to_db(self):
        district_list = self.parse_districts()
        to_load_data = []
        for district in district_list:
            ISOTIMEFORMAT = "%Y-%m-%d %X"
            to_load_data.append({'district':district,'district_name':district_list[district], 'city':self.city, 'update_time':time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))})
        print to_load_data
        LjDistrict.loadData(to_load_data)





if __name__ == "__main__":
    print 'is the file'
    district = DistrictSpider('bj')
    district.save_to_db()