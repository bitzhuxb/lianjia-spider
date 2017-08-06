#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert

Base = declarative_base()
engine = create_engine(config.DB_CONNECT_STRING, echo=config.DB_ECHO)


class DailyYahooModel(Base):
    __tablename__ = 'daily_yahoo_stock'
    date = Column(Date, primary_key=True)
    stock = Column(String(100),primary_key=True)
    low = Column(Float)
    high = Column(Float)
    open = Column(Float)
    close = Column(Float)
    volume = Column(Integer)

    #decorator replace into 的方式
    @compiles(Insert)
    def replace_string(insert, compiler, **kw):
        s = compiler.visit_insert(insert, **kw)
        s = s.replace("INSERT INTO", "REPLACE INTO")
        return s

    @classmethod
    def setup(cls):
        Base.metadata.create_all(engine)

    @classmethod
    def loadData(cls, data):
        DB_Session = sessionmaker(bind=engine)
        session = DB_Session()
        session.execute(
            cls.__table__.insert(replace_string=""), data
        )
        session.commit()

if __name__ == "__main__":
    DailyYahooModel.setup()
    data = {
        'date':'2017-01-02',
        'stock':'test',
        'low':123,
        'high':345,
        'open':1234.3,
        "close":1234.45,
        'volumn':234
    }

    DailyYahooModel.loadData(data)
