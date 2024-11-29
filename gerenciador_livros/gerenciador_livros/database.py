from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from gerenciador_livros.settings import Settings

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega o arquivo .env

print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")


# Configuração das variáveis de ambiente
settings = Settings()

# Configuração do engine e da sessão
engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True para debug
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para fornecer uma sessão de banco de dados
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
