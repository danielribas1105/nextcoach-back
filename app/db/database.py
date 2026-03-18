from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Engine para a APLICAÇÃO — usa conexão pooled + NullPool
# O Neon já gerencia o pool via PgBouncer, não precisamos de pool no SQLAlchemy
engine = create_engine(
   settings.db_url,
   poolclass=NullPool,       # desativa pool do SQLAlchemy (Neon cuida disso)
   connect_args={
      "sslmode": "require"  # Neon exige SSL obrigatoriamente
   }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()