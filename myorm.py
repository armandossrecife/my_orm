# Import the necessary modules
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Establish a database connection
database_url = "sqlite:///myteste.db"

# Create an engine to connect to a SQLite database
engine = create_engine(database_url)

# Retorna a instancia do engine
Base = declarative_base()

# Define your data model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Create the database tables
Base.metadata.create_all(engine)

# Insert data into the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a new user in the database
new_user = User(username='Sandy', email='sandy@gmail.com')
session.add(new_user)
session.commit()

# Query data from the database
all_users = session.query(User).all()

# Query a spectific user by their username 
user = session.query(User).filter_by(username='Sandy').first()

# Close the session
session.close