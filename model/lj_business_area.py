import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config import config
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(config.DB_CONNECT_STRING, echo=config.DB_ECHO)
class LjBusinessArea(Base):
    __tablename__ = 'lj_business_area'
    business_area = Column(String(500),primary_key=True)
    business_area_name = Column(String(1000))
    district = Column(String(1000))
    update_time = Column(DateTime)
    @classmethod
    def setup(cls):
        Base.metadata.create_all(engine)
    @classmethod
    def loadData(cls, data):
        DB_Session = sessionmaker(bind=engine)
        session = DB_Session()
        session.execute(
           LjBusinessArea.__table__.insert().prefix_with('IGNORE'),data
        )
        session.commit()
if __name__ == "__main__":
    LjBusinessArea.setup()