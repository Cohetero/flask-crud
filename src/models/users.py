from sqlalchemy import Column, Integer, String
from settings.common import Base

class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer(), primary_key = True)
    name = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    foto = Column(String(500), nullable = True)

    def __str__(self):
        return f"User (name={self.name}, email={self.email})"