# -*- coding: utf-8 -*-

import re
import urllib2
import random
import threading
import logging
from bs4 import BeautifulSoup
from model.lj_business_area import LjBusinessArea
from lianjia.district_spider import DistrictSpider
from time import sleep
import time
from utils.urllib_tool import UrllibTool


import sys
reload(sys) #疑问
sys.setdefaultencoding("utf8")
sys.path.append("..")
import config.config
hds = config.config.hds
class BusinessAreaSpider(object) :

    def __init__(self,city,district):
        self.city = city
        self.plain_text = None
        self.district = district
    def get_url(self):

        return u'http://'+ self.city + '.lianjia.com/chengjiao/'+ self.district
    def get_page_content(self):
        print self.get_url()
        return UrllibTool.get_page_content(self.get_url())
    def parse_busi_areas(self):
        self.plain_text = self.get_page_content()
        print self.plain_text
        soup = BeautifulSoup(self.plain_text, "html.parser")
        busi_area_soup_list = soup.find('div', {'data-role': 'ershoufang'}).find_all('div')[1].find_all('a')
        busi_area_list = {}
        for busi_area in busi_area_soup_list:
            busi_area_id = busi_area.attrs['href'].replace('/chengjiao/','').replace('/','')
            busi_area_name = busi_area.text
            print busi_area_name
            busi_area_list[busi_area_id] = busi_area_name
        return busi_area_list

    def save_to_db(self):
        busi_area_list = self.parse_busi_areas()
        to_load_data = []
        for busi_area in busi_area_list:
            ISOTIMEFORMAT = "%Y-%m-%d %X"
            to_load_data.append({'business_area':busi_area, 'business_area_name':busi_area_list[busi_area], 'district':self.district, 'update_time':time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))})
        print to_load_data
        LjBusinessArea.loadData(to_load_data)





if __name__ == "__main__":
    print 'is the file'

    district = DistrictSpider('bj')
    district_list = district.parse_districts()
    for district_id in district_list:
        busi_area = BusinessAreaSpider('bj', district_id)
        busi_area.save_to_db()
        time.sleep(10)



 #   district = BusinessAreaSpider('bj','dongcheng')
 #   district.save_to_db()