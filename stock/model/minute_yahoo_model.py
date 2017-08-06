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


class MinuteYahooModel(Base):
    __tablename__ = 'minute_yahoo_stock'
    date = Column(Date, primary_key=True)
    stock = Column(String(100),primary_key=True)
    time = Column(MEDIUMTEXT)
    low = Column(MEDIUMTEXT)
    high = Column(MEDIUMTEXT)
    open = Column(MEDIUMTEXT)
    close = Column(MEDIUMTEXT)
    volume = Column(MEDIUMTEXT)

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
    MinuteYahooModel.setup()
    data = {
        'date':'2017-01-02',
        'stock':'date',
        'time':'sdfssdddsddf',
        'low':'dd',
        'high':'hidddd',
        'open':'open',
        "close":'close'
    }

    MinuteYahooModel.loadData(data)
