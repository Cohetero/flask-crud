from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:secret@localhost/personas')
meta = MetaData()
conn = engine.connect()