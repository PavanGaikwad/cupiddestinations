from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class Destination(Base):
    __tablename__ = "destinations"
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    desc = Column(Text)
    summary = Column(Text)
    image_url = Column(String(1024))
    tags = Column(String(80))

    def __init__(self, name, desc, summary, image_url,tags):
    	self.name = name
    	self. desc = desc
        self.tags = tags
        self.image_url = image_url
        self.summary = summary
        

    # def __repr__(self):
    #     return ""

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if k!="_sa_instance_state"])