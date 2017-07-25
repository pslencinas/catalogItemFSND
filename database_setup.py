from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))

class Genre(Base):
	__tablename__ = 'genre'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	
	@property
	def serialize(self):
	   """return object data in easily serializeable format"""
	   return {
	   		'name'		:	self.name,
	   		'id'		:	self.id
	   }

class Movie(Base):
    __tablename__ = 'movie'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    overview = Column(String(500))
    director = Column(String(80))
    youtube_url = Column(String(250))
    poster_url = Column(String(250))
    genre_id = Column(Integer,ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'         : self.id,
           'overview'	: self.overview,
           'director'	: self.director,
           'poster_url' : self.poster_url,
           'youtube_url'	: self.youtube_url
       }

engine = create_engine('sqlite:///moviedump.db')

Base.metadata.create_all(engine)
