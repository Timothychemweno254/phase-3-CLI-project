from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    
    skills = relationship('Skill', back_populates='user', cascade='all, delete-orphan')

class Skill(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    goal_description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship('User', back_populates='skills')
    learning_lessons = relationship('LearningLesson', back_populates='skill', cascade='all, delete-orphan')

class LearningLesson(Base):
    __tablename__ = 'learning_lessons'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    content = Column(Text, nullable=False)
    duration = Column(Integer, nullable=False) 
    notes = Column(Text, nullable=True)

    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)
    skill = relationship('Skill', back_populates='learning_lessons')
