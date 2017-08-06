#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class YahooUtil:
    @staticmethod
    # 判断雅虎的返回结果是否有效
    def is_stock_result_exist(content_json):
        if not content_json:
            return False
        content = json.loads(content_json)
        if content.get('chart').get('error'):
            return False
        if not content['chart']['result'][0].get('timestamp'):
            return False
        return True

