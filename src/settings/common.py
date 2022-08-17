from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('mysql+pymysql://root:secret@localhost/personas')
Base = declarative_base()
Session = sessionmaker(engine)
