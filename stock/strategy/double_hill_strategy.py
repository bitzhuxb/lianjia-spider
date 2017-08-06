#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import pandas as pg
from utils.stock_util import StockUtil

class HistoryDoubleHillStrategy():
    def __init__(self,data, begin_minute = 11, end_minute = 300, first_hill_up_percent = 15, second_stop_loss_percent = 0.02):
        self.data = data
        self.begin_minute = begin_minute
        self.end_minute = end_minute
        self.second_stop_loss_percent = second_stop_loss_percent
        self.first_hill_up_percent = first_hill_up_percent
        self.stop_loss = False
        self.second_stop_loss = False
        self.first_top = False
        self.begin_trace = False
        self.buy_point = False
        self.sell_point = False

        self._init_process()

    def _init_process(self):
        pass

    def _trans_to_dataframe(self):
        self.df_data = DataFrame(self.data)

    def re_run_data_process(self):
        pass


    def find_begin_trace(self):

        begin_index = self.begin_minute
        begin_trace = False

        for i in range(self.begin_minute ,min(len(self.data['time']), self.end_minute)):
            if StockUtil.compare_previous_index(data['low'],data['high'],i):
                if StockUtil.percent_bigger(data['low'], data['high'], begin_index, i, self.first_hill_up_percent):
                    self.begin_trace = i
                    print i
                    return i
            else:
                begin_index = i
        return False

    def find_first_top(self):
        self.first_top = False
        for i in range(self.begin_trace+1, min(len(self.data['time']), self.end_minute)):
            if StockUtil.compare_previous_index(data['low'], data['high'], i):
                self.first_top = i
            else:
                return self.first_top
        return False

    def find_first_stop_loss(self):
        self.stop_loss = False
        for i in range(self.first_top + 1, min(len(self.data['time']), self.end_minute)):
            if StockUtil.compare_previous_index(data['low'], data['high'], i):
                return self.stop_loss
            elif StockUtil.compare_specified_index(data['low'], data['high'], i, self.begin_trace):
                self.stop_loss = i
            else:
                return False
        return False

    def find_buy_point(self):
        self.buy_point = False
        self.second_stop_loss = False
        for i in range(self.stop_loss + 1, min(len(self.data['time']), self.end_minute)):
            if StockUtil.compare_previous_index(data['low'], data['high'], i):
                if StockUtil.compare_specified_index(data['low'], data['high'], i, self.first_top):
                    self.buy_point = i
                    self.second_stop_loss = (data['low'][i] + data['high'][i]) *  (1-self.second_stop_loss_percent) /2
                    return self.buy_point
            else:
                return False

    def find_sell_point(self):
        self.sell_point = None
        for i in range(self.buy_point + 1, min(len(self.data['time']), self.end_minute)):
            if StockUtil.compare_previous_index(data['low'], data['high'], i):
                if self.second_stop_loss < (data['low'][i] + data['high'][i]) * (1 - self.second_stop_loss_percent) /2:
                    self.second_stop_loss = (data['low'][i] + data['high'][i]) *  (1-self.second_stop_loss_percent) /2
            else:
                if self.second_stop_loss > (data['low'][i] + data['high'][i])/2 or StockUtil.compare_specified_index(data['low'], data['high'], i, self.stop_loss):
                    self.sell_point = i
        self.sell_point = min(len(self.data['time']), self.end_minute)
        return self.sell_point





if __name__ == '__main__':
    data = {
        "time":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        "low":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        "high":[2,3,4,5,6,7,8,9,0,4,5,6,7,8,9,0,11,3,23,4,5]
    }

    ins = HistoryDoubleHillStrategy(data)
    ins.find_begin_trace()