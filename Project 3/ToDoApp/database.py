

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
SQLALCHEMY_DATABASE_URL="postgresql://postgres:python@localhost/TodoDatabase"

# SQLALCHEMY_DATABASE_URI=postgresql://fast_api:fast_api1234@localhost/lv_billing
# SQLALCHEMY_TEST_DATABASE_URI=postgresql://fast_api:fast_api1234@localhost/lv_billing_test
# where fast_api is db username
# fast_api1234 is password
# lv_billing , lv_billing_test are database created.


# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()