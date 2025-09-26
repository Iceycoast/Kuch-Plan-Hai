from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class Category(Base):

    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable= False, index=True)
    slug = Column(String(100), unique=True, nullable = False, index= True)
    sort_order = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Category(category_id={self.category_id}, name='{self.name}')>"