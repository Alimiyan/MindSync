from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Node(Base):
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    mindmap_id = Column(Integer, ForeignKey('mindmap.id'))
    mindmap = relationship("MindMap", back_populates="nodes")
