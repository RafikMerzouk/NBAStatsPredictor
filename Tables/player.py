from sqlalchemy import Column, Integer, String, Sequence
from . import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    full_name = Column(String(50))
    team_id = Column(Integer)
