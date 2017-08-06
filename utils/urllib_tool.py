import re
import urllib2
import random
import threading
import logging
from time import sleep
import config.config
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import config.stock_config
from config.stock_config import logging


class UrllibTool(object):
    @staticmethod
    def get_page_content(page_url,timeout = 30, headers = None):

        if headers == None:
            hds = config.config.hds
            headers = hds[random.randint(0, len(hds) - 1)]
        try:

            req = urllib2.Request(page_url, headers = headers)
            source_code = urllib2.urlopen(req, timeout = timeout).read()
            plain_text = unicode(source_code)  # ,errors='ignore')
            return plain_text

        except (urllib2.HTTPError, urllib2.URLError), e:
            warning = {'page_url':page_url,'error':e}
            logging.warning(warning)
            return None
        except Exception, e:

            warning = {'page_url':page_url,'error':e}
            logging.warning(warning)
            return None


if __name__ == "__main__":
    UrllibTool.get_page_content(u"https://query1.finance.yahoo.com/v8/finance/chart/AKCA?range=1d&interval=1m")