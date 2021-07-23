# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as delta
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, Boolean, func,update
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship

from common.database import Base, get_ulid,session

class BookItem(Base):
    __tablename__ = 'book_item'
    mysql_charset='utf8mb4',
    mysql_collate='utf8mb4_unicode_ci'
    
    id = Column(String(32), primary_key=True, default=get_ulid)
    title = Column('title',String(100),nullable=False)
    isbn = Column('isbn',String(20),nullable=False)
    jan = Column('jan',String(20),nullable=True)
    author = Column('author',String(20),nullable=False)
    description = Column('description',String(1024),nullable=True)
    
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=current_timestamp(), onupdate=func.utc_timestamp())
