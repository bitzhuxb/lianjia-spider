# -*- coding: utf-8 -*-

import re
import urllib2
import random
import threading
import logging
from bs4 import BeautifulSoup
from model.lj_deal import LjDeal
from time import sleep


import sys
reload(sys) #疑问
sys.setdefaultencoding("utf-8")
sys.path.append("..")
import config.config
hds = config.config.hds

class DealSpider(object):
    def __init__(self, page_num, url_prefix):
        self.page_num = page_num
        self.url_prefix = url_prefix
        self.page_url = self.url_prefix + str(self.page_num)
        self.plain_text = ''
        self.all_list_info = []
    def get_page_content(self):
        """
        打开并获取链接内容
        """
        try:
            req = urllib2.Request(self.page_url,headers=hds[random.randint(0,len(hds)-1)])
            source_code = urllib2.urlopen(req,timeout=10).read()
            plain_text=unicode(source_code)#,errors='ignore')
            self.plain_text = plain_text;
            soup = BeautifulSoup(plain_text, "html.parser")
            return plain_text

        except (urllib2.HTTPError, urllib2.URLError), e:
            print e
          #  exception_write('chengjiao_spider',url_page)
            return
        except Exception,e:
            print e
           # exception_write('chengjiao_spider',url_page)
            return

    def save_to_db(self):
        print self.all_list_info
        LjDeal.loadData(self.all_list_info)
        return 0
    def parse_cols(self):
        try:

            soup = BeautifulSoup(self.plain_text, "html.parser")

            deal_list = soup.findAll('div', {'class': 'info'})
            for deal in deal_list:
                info_dict = {}
                href = deal.find('a')
                if not href:
                    continue
                #处理链接和文本
                info_dict['link'] = href.attrs['href']
                info_dict['desc'] = href.text



# """
# <div class="info">
#     <div class="title">
#         <a href="http://bj.lianjia.com/chengjiao/101101066809.html" target="_blank">丽都东镇滨河1号 1室0厅 55.58平米</a>
#     </div>
#     <div class="address">
#         <div class="houseInfo">
#             <span class="houseIcon"></span>西 | 毛坯&nbsp;| 有电梯
#         </div>
#     <div class="dealDate">2017.03.19</div>
#     <div class="totalPrice"><span class="number">240</span>万</div>
#     </div>
#     <div class="flood">
#         <div class="positionInfo">
#             <span class="positionIcon"></span>高楼层(共7层) 2010年建板楼
#         </div>
#         <div class="source">链家成交</div>
#         <div class="unitPrice"><span class="number">43182</span>元/平</div>
#         </div>
#         <div class="dealHouseInfo">
#             <span class="dealHouseIcon"></span>
#             <span class="dealHouseTxt"><span>房屋满五年</span></span></div>
#         <div class="dealCycleeInfo">
#             <span class="dealCycleIcon"></span>
#             <span class="dealCycleTxt"><span>挂牌246万</span>
#             <span>成交周期67天</span></span>
#
#         </div></div>
# """

                info_dict['deal_date'] = deal.find('div', {'class': 'dealDate'}).text.replace('.','-')
                info_dict['sell_price'] = deal.find('div', {'class': 'totalPrice'}).find('span',{'class':'number'}).text
                info_dict['house_info'] = deal.find('div', {'class': 'houseInfo'}).text
                info_dict['position_info'] = deal.find('div', {'class': 'positionInfo'}).text
                info_dict['source'] = deal.find('div', {'class': 'source'}).text
                info_dict['house_year'] = deal.find('div',{'class':'dealHouseInfo'})
                deal_house_info = deal.find('div',{'class':'dealHouseInfo'})
                if(deal_house_info):
                    info_dict['house_year'] = deal_house_info.text
                else:
                    info_dict['house_year'] = ''
                info_dict['deal_cycle_price'] = deal.find('div', {'class': 'dealCycleeInfo'}).find('span',{'class':'dealCycleTxt'}).find_all('span')[0].text
                info_dict['cycle_price'] = unicode(info_dict['deal_cycle_price'])
                info_dict['cycle_time'] = deal.find('div', {'class': 'dealCycleeInfo'}).find('span',{'class':'dealCycleTxt'}).find_all('span')[1].text

                    #   info_dict['unit_price'] = deal.find('div', {'class': 'unitPrice'}).find('span',{'class':'number'}).text
              #  info_dict['deal_cycle'] = deal.find('span', {'class': 'dealHouseTxt'}).text
              #  info_dict['list_price'] = deal.find('span', {'class': 'dealCycleeInfo'}).text
               # for key in info_dict:
                self.all_list_info.append(info_dict)

#        if len(info_dict)












                '''



                content = cj.find('h2').text.split()
                if content:
                    info_dict.update({u'小区名称': content[0]})
                    info_dict.update({u'户型': content[1]})
                    info_dict.update({u'面积': content[2]})
                content = unicode(cj.find('div', {'class': 'con'}).renderContents().strip())
                content = content.split('/')
                if content:
                    info_dict.update({u'朝向': content[0].strip()})
                    info_dict.update({u'楼层': content[1].strip()})
                    if len(content) >= 3:
                        content[2] = content[2].strip();
                        info_dict.update({u'建造时间': content[2][:4]})
                content = cj.findAll('div', {'class': 'div-cun'})
                if content:
                    info_dict.update({u'签约时间': content[0].text})
                    info_dict.update({u'签约单价': content[1].text})
                    info_dict.update({u'签约总价': content[2].text})
                content = cj.find('div', {'class': 'introduce'}).text.strip().split()

                if content:
                    for c in content:
                        if c.find(u'满') != -1:
                            info_dict.update({u'房产类型': c})
                        elif c.find(u'学') != -1:
                            info_dict.update({u'学区': c})
                        elif c.find(u'距') != -1:
                            info_dict.update({u'地铁': c})
                                '''

        except Exception, e:
            print e



"""



def chengjiao_spider(db_cj,url_page=u"http://bj.lianjia.com/chengjiao/pg1rs%E5%86%A0%E5%BA%AD%E5%9B%AD"):

    try:
        req = urllib2.Request(url_page,headers=hds[random.randint(0,len(hds)-1)])
        source_code = urllib2.urlopen(req,timeout=10).read()
        plain_text=unicode(source_code)#,errors='ignore')   
        soup = BeautifulSoup(plain_text)
    except (urllib2.HTTPError, urllib2.URLError), e:
        print e
        exception_write('chengjiao_spider',url_page)
        return
    except Exception,e:
        print e
        exception_write('chengjiao_spider',url_page)
        return

    cj_list=soup.findAll('div',{'class':'info-panel'})
    for cj in cj_list:
        info_dict={}
        href=cj.find('a')
        if not href:
            continue
        info_dict.update({u'链接':href.attrs['href']})
        content=cj.find('h2').text.split()
        if content:
            info_dict.update({u'小区名称':content[0]})
            info_dict.update({u'户型':content[1]})
            info_dict.update({u'面积':content[2]})
        content=unicode(cj.find('div',{'class':'con'}).renderContents().strip())
        content=content.split('/')
        if content:
            info_dict.update({u'朝向':content[0].strip()})
            info_dict.update({u'楼层':content[1].strip()})
            if len(content)>=3:
                content[2]=content[2].strip();
                info_dict.update({u'建造时间':content[2][:4]}) 
        content=cj.findAll('div',{'class':'div-cun'})
        if content:
            info_dict.update({u'签约时间':content[0].text})
            info_dict.update({u'签约单价':content[1].text})
            info_dict.update({u'签约总价':content[2].text})
        content=cj.find('div',{'class':'introduce'}).text.strip().split()
        if content:
            for c in content:
                if c.find(u'满')!=-1:
                    info_dict.update({u'房产类型':c})
                elif c.find(u'学')!=-1:
                    info_dict.update({u'学区':c})
                elif c.find(u'距')!=-1:
                    info_dict.update({u'地铁':c})

        command=gen_chengjiao_insert_command(info_dict)
        db_cj.execute(command,1)
"""



if __name__ == "__main__":
    print ('this is the mail file')
    for i in range(1,100):
        page_ins = DealSpider(i,'http://bj.lianjia.com/chengjiao/pg')
        content = page_ins.get_page_content()
        print i
        page_ins.parse_cols()
        page_ins.save_to_db()
        sleep(60)