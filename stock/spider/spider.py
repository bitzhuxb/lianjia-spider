# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from utils.urllib_tool import UrllibTool
class Spider:
    #stock 代表股票标识
    def __init__(self, stock):
        self.stock = stock

    def generate_url(self):
        pass

    def get_content(self):
        url = self.generate_url();
        self.content = UrllibTool.get_page_content(url);
        return self.content

    def parse_content_to_dict(self):
        pass





