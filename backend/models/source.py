from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(Enum("rss", "web", "email", name="source_type"), nullable=False)
    config = Column(JSON, nullable=False)
    schedule = Column(String, default="daily")

    summaries = relationship("Summary", back_populates="source")

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("sources.id"))
    fetched_at = Column(DateTime, default=datetime.utcnow)
    title = Column(String)
    content = Column(Text)
    summary = Column(Text)

    source = relationship("Source", back_populates="summaries")

