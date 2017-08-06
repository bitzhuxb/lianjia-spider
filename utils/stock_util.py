#!/usr/bin/env python
# -*- coding: utf-8 -*-
class StockUtil:
    #TODO 添加异常处理逻辑
    @staticmethod
    def compare_previous_index(low, high, index):
        # print index
        # #自生自灭吧...抛出异常，暂时不处理了
        # print low[index],high[index],low[index] + high[index]
        # print low[index-1],high[index-1],low[index-1] + high[index-1]

        if low[index] + high[index] - (low[index-1] + high[index-1]) > 0 :
            return True
        else:
            return False

    @staticmethod
    def compare_specified_index(low, high, begin_index, end_index):
        if low[begin_index] + high[begin_index] - (low[end_index] + high[end_index]) > 0 :
            return True
        else:
            return False


    #比较某两个下标的差异性
    @staticmethod
    def percent_bigger(low, high, begin_index, end_index, percent):
        if (low[end_index] + high[end_index] - low[begin_index] - high[begin_index]) * 100 / (low[begin_index] + high[begin_index]) > percent:
            return True
        else:
            return False





