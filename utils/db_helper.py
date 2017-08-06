# -*- coding: utf-8 -*-
import re
import urllib2
import random
import threading
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config


class DBHelper(object):
    def __init__(self, command, echo = False):
       # self.lock = threading.RLock()  # 锁
        self.ret = None;
        if command != '':
            session = self.get_session(echo)
            self.ret = session.execute(command)
            self.session_close(session)

        # session.execute('create database spider')

    def get_session(self, echo=True):
        engine = create_engine(config.DB_CONNECT_STRING, echo=echo)
        DB_Session = sessionmaker(bind=engine)
        session = DB_Session()
        return session

    def session_close(self,session=None):
        session.close()




if __name__ == "__main__":
    db_ins = DBHelper('create database zxbtest')
    db_ins = DBHelper('drop database zxbtest')
    print db_ins.ret