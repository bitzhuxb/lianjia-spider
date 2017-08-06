import sqlalchemy
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config import config
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(config.DB_CONNECT_STRING, echo=config.DB_ECHO)
class LjDeal(Base):
    __tablename__ = 'lj_model'
    cycle_time = Column(String(100))
    desc = Column(String(1000))
    sell_price = Column(Integer)
    source = Column(String(100))
    link = Column(String(500),primary_key=True)
    position_info = Column(String(1000))
    house_info = Column(String(1000))
    house_year = Column(String(100))
    deal_cycle_price = Column(String(100))
    deal_date = Column(Date)


    @classmethod
    def setup(cls):
        Base.metadata.create_all(engine)
    @classmethod
    def loadData(cls, data):
        DB_Session = sessionmaker(bind=engine)
        session = DB_Session()
        session.execute(
           LjDeal.__table__.insert().prefix_with('IGNORE'),data
        )
        session.commit()
if __name__ == "__main__":
    LjDeal.setup()