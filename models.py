from sqlalchemy import Column, Integer, String, Text, Date, Numeric, ForeignKey, func, desc
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

###################################################




class ExchangeRatesTable(Base):
    __tablename__= 'exchange_rates_table'
    
    id = Column(Integer, primary_key=True)
    type = Column(String(1), nullable=False)
    number = Column(Text, nullable=False, unique=True)
    date = Column(Date, nullable=False)
    
    rates = relationship('ExchangeRate', 
                        back_populates='table',
                        cascade='all, delete, delete-orphan')

class ExchangeRate(Base):
    __tablename__ = 'exchange_rate'
    id = Column(Integer, primary_key=True)
    value = Column(Text) #Dialect sqlite+pysqlite does *not* support 
                        #Decimal objects natively, and SQLAlchemy must 
                        #convert from floating point - rounding errors 
                        #and other issues may occur. Please consider 
                        #storing Decimal numbers as strings or integers 
                        #on this platform for lossless storage.
    table_id = Column(Integer, ForeignKey('exchange_rates_table.id'))
    table = relationship('ExchangeRatesTable', back_populates='rates')
    currency_id = Column(Integer, ForeignKey('currency.id'))
    currency = relationship('Currency', back_populates='rates')
        

class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    code = Column(String(3), nullable=False, unique=True)
    rates = relationship('ExchangeRate', back_populates='currency')
    

    
    
    


    
