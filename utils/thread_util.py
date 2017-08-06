#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import threading
def load_all_data(self, func, *args, ):
    list = self.get_all_stock()
    thread_list = []
    begin = time.time()
    print len(list)
    for stock in list:
        # thread_list.append(threading.Thread(target=YahooStockService.load_minute_stock,args=(stock,)))
        thread_list.append(threading.Thread(target=func, args=args))

        # YahooStockService.load_one_stock(stock)
    i = 0
    for t in thread_list:
        t.setDaemon(True)
        t.start()
        i = i + 1
        if i >= 10:
            i = 0
            t.join()
    t.join()
    print time.time() - begin, "ctime"
