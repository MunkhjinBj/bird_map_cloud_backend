from sqlalchemy import Column, Integer, String, JSON
from geoalchemy2 import Geometry
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Species(Base):
    __tablename__ = "species"
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    metadata = Column(JSON)

class SeasonalRange(Base):
    __tablename__ = "seasonal_ranges"
    id = Column(Integer, primary_key=True)
    species_id = Column(Integer)
    season = Column(String)
    geom = Column(Geometry("MULTIPOLYGON", srid=4326))
    source = Column(String)
