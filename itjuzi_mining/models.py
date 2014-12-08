from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

import settings

DeclarativeBase = declarative_base()

investfirms_investevents_table = Table('investfirms_investevents', DeclarativeBase.metadata,
    Column('investfirms_id', Integer, ForeignKey('investfirms.id')),
    Column('investevents_id', Integer, ForeignKey('investevents.id'))
)

class Investevent(DeclarativeBase):
    __tablename__ = "investevents"

    id = Column(Integer, primary_key=True)
    date = Column(String)
    turn = Column(String)
    money = Column(String)
    area = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))

class Mergeevent(DeclarativeBase):
    __tablename__ = 'mergeevents'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    money = Column(String)
    area = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))
    investfirm_id = Column(Integer, ForeignKey('investfirms.id'))

class Company(DeclarativeBase):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    url = Column(String)
    date = Column(String)
    location = Column(String)
    state = Column(String)
    area = Column(String)
    stage = Column(String)
    tags = Column(String)
    discr = Column(String)
    investevents = relationship('Investevent', backref='company' )
    mergeevent = relationship('Mergeevent', uselist=False, backref='company')

class Investfirm(DeclarativeBase):
    __tablename__ = "investfirms"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    url = Column(String)
    stages = Column(String)
    areas = Column(String)
    investevents = relationship('Investevent',
                                secondary=investfirms_investevents_table,
                                backref='investfirms' )
    mergeevents = relationship('Mergeevent', backref='investfirm')
