#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests

class ZhongriDoctor:
    def __init__(self, departmentId =200041952,  data = None, headers = None):
        if headers is None:
            headers = {}
            headers['Cookie'] ='SESSION_COOKIE=3cab1829cea36edbceb07f7e; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500853202; JSESSIONID=93DC8ED2C49157316ABE5314FEB5D7CC'
            headers['Origin'] = "http://www.bjguahao.gov.cn"
            headers['Accept-Encoding'] = "gzip, deflate"
            headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
            headers['Referer'] = 'http://www.bjguahao.gov.cn/dpt/appoint/270-'+ str(departmentId) + '.htm'
            headers['X-Requested-With'] = 'XMLHttpRequest'
            headers['Connection'] = 'keep-alive'
            #self.cookies = dict(SESSION_COOKIE='3cab1829cea36edbceb07f7e',Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa='1500423799,1500809867,1500809963,1500810824',Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500812440,JSESSIONID='8AE0A6573279886498402B6D04B91A6C')
            #curl 'http://www.bjguahao.gov.cn/dpt/partduty.htm' -H 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500812440; JSESSIONID=8AE0A6573279886498402B6D04B91A6C' -H 'Origin: http://www.bjguahao.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://www.bjguahao.gov.cn/dpt/appoint/270-200003913.htm' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'hospitalId=270&departmentId=200003913&dutyCode=2&dutyDate=2017-07-31&isAjax=true' --compressed
        if data is None:
            data = {}
            data['hospitalId'] = 270
            data['departmentId'] = departmentId
            #TODO change
            data['dutyCode'] = 1
            # TODO change
            data['dutyDate'] = '2017-07-25'
            data['isAjax'] = 'true';
        self.data = data
        self.headers = headers
    def get_doctor_info(self):
        ret = requests.post('http://www.bjguahao.gov.cn/dpt/partduty.htm', data = self.data, headers = self.headers)
        ret_arr = json.loads(ret.text)
        print ret.text
        doctor_id = ret_arr['data'][0]['doctorId']
        duty_id = ret_arr['data'][0]['dutySourceId']
        departmentId = ret_arr['data'][0]['departmentId']
        self.duty_id = duty_id
        self.departmentId = departmentId
        self.doctor_id = doctor_id
        ret = "http://www.bjguahao.gov.cn/order/confirm/270-"+ str(departmentId) + "-" + str(doctor_id) + '-' + str(duty_id) + '.htm'
        print ret




    def send_message(self):
        url = self.get_doctor_info()
        headers = self.headers
        headers['Referer'] = url
        headers['Content-Length'] = '0'
        self.headers = headers
        ret = requests.post('http://www.bjguahao.gov.cn/v/sendorder.htm', headers=headers)
        print ret.text
        print ret

    # curl
    # 'http://www.bjguahao.gov.cn/order/confirm.htm' - H
    # 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; JSESSIONID=8AE0A6573279886498402B6D04B91A6C; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500816994' - H
    # 'Origin: http://www.bjguahao.gov.cn' - H
    # 'Accept-Encoding: gzip, deflate' - H
    # 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' - H
    # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' - H
    # 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' - H
    # 'Accept: application/json, text/javascript, */*; q=0.01' - H
    # 'Referer: http://www.bjguahao.gov.cn/order/confirm/270-200003913-200657988-44549076.htm' - H
    # 'X-Requested-With: XMLHttpRequest' - H
    # 'Connection: keep-alive' - -data
    # 'dutySourceId=44549076&hospitalId=270&departmentId=200003913&doctorId=200657988&patientId=233133096&hospitalCardId=&medicareCardId=120749265008&reimbursementType=1&smsVerifyCode=wer&childrenBirthday=&isAjax=true' - -compressed
    #
    # curl
    # 'http://www.bjguahao.gov.cn/order/confirm.htm' - H
    # 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; JSESSIONID=8AE0A6573279886498402B6D04B91A6C; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500816994' - H
    # 'Origin: http://www.bjguahao.gov.cn' - H
    # 'Accept-Encoding: gzip, deflate' - H
    # 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' - H
    # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' - H
    # 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' - H
    # 'Accept: application/json, text/javascript, */*; q=0.01' - H
    # 'Referer: http://www.bjguahao.gov.cn/order/confirm/270-200003913-200657988-44549076.htm' - H
    # 'X-Requested-With: XMLHttpRequest' - H
    # 'Connection: keep-alive' - -data
    # 'dutySourceId=44549076&hospitalId=270&departmentId=200003913&doctorId=200657988&patientId=233133096&hospitalCardId=&medicareCardId=120749265008&reimbursementType=1&smsVerifyCode=wer&childrenBirthday=&isAjax=true' - -compressed
    def commit(self):
        self.send_message()
        headers = self.headers
        headers.pop('Content-Length')
        data = {}
        data['dutySourceId'] = self.duty_id
        data['hospitalId'] = 270
        data['departmentId'] = self.departmentId
        data['doctorId'] = self.doctor_id
        data['patientId'] = 233133096
        data['medicareCardId'] = 120749265008
        data['reimbursementType'] = 1
        # TODO
        data['smsVerifyCode'] = 123
        data['childrenBirthday'] = ''
        data['isAjax'] = "true"

        # curl
        # 'http://www.bjguahao.gov.cn/order/confirm.htm' - H
        # 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; JSESSIONID=8AE0A6573279886498402B6D04B91A6C; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500820210' - H
        # 'Origin: http://www.bjguahao.gov.cn' - H
        # 'Accept-Encoding: gzip, deflate' - H
        # 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' - H
        # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' - H
        # 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' - H
        # 'Accept: application/json, text/javascript, */*; q=0.01' - H
        # 'Referer: http://www.bjguahao.gov.cn/order/confirm/270-200003913-200657988-44549076.htm' - H
        # 'X-Requested-With: XMLHttpRequest' - H
        # 'Connection: keep-alive' - -data
        # 'dutySourceId=44549076&hospitalId=270&departmentId=200003913&doctorId=200657988&patientId=233133096&hospitalCardId=&medicareCardId=&reimbursementType=1&smsVerifyCode=123&childrenBirthday=&isAjax=true' - -compressed

        #ret = requests.post('http://www.bjguahao.gov.cn/order/confirm.htm', headers=headers, data=data)
        print ret.text
        print ret


        print data
        print headers





#     def send_message(self):
#
#
# curl 'http://www.bjguahao.gov.cn/v/sendorder.htm' -X POST
# -H 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; JSESSIONID=8AE0A6573279886498402B6D04B91A6C; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500816994'
# -H 'Origin: http://www.bjguahao.gov.cn'
# -H 'Accept-Encoding: gzip, deflate'
# -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'
# -H 'Accept: application/json, text/javascript, */*; q=0.01'
# -H 'Referer: http://www.bjguahao.gov.cn/order/confirm/270-200003913-200657988-44549076.htm'
# -H 'X-Requested-With: XMLHttpRequest'
# -H 'Connection: keep-alive'
# -H 'Content-Length: 0' --compressed


ins = ZhongriDoctor();

ret = ins.commit()







# curl 'http://www.bjguahao.gov.cn/dpt/partduty.htm' -H 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; JSESSIONID=D0CA5685BA0949E948EFA3E500F456FC; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1499261341,1499261367,1500423799; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500424830' -H 'Origin: http://www.bjguahao.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://www.bjguahao.gov.cn/dpt/appoint/270-200003875.htm' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'hospitalId=270&departmentId=200041952&dutyCode=1&dutyDate=2017-07-20&isAjax=true' --compressed
# curl 'http://www.bjguahao.gov.cn/dpt/partduty.htm' -H 'Cookie: SESSION_COOKIE=3cab1829cea36edbceb07f7e; JSESSIONID=E8C4B69A0B68087C88BABC9C7D474531; Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500423799,1500809867,1500809963,1500810824; Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa=1500812440'
# -H 'Origin: http://www.bjguahao.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01'
# -H 'Referer: http://www.bjguahao.gov.cn/dpt/appoint/270-200003913.htm' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive'
# --data 'hospitalId=270&departmentId=200041952&dutyCode=1&dutyDate=2017-07-24&isAjax=true' --compressed