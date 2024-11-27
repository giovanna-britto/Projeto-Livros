from sqlalchemy import Column, Integer, String, Float  # Importa os tipos de dados e funcionalidades do SQLAlchemy
from gerenciador_livros.database import Base  # Importa a classe base para os modelos do banco de dados

# Define a classe Book que representa a tabela "books" no banco de dados
class Book(Base):
    __tablename__ = "books"  # Define o nome da tabela no banco de dados como "books"

    # Colunas da tabela (mapeamento para atributos da classe)
    id = Column(Integer, primary_key=True, index=True)  # Coluna "id", chave primária, índice único
    title = Column(String, nullable=False)  # Coluna "title" (string), não permite valores nulos
    author = Column(String, nullable=False)  # Coluna "author" (string), não permite valores nulos
    year = Column(Integer, nullable=False)  # Coluna "year" (inteiro), não permite valores nulos
    isbn = Column(String, unique=True, nullable=False)  # Coluna "isbn" (string), deve ser única e não permite valores nulos
    category = Column(String, nullable=False)  # Coluna "category" (string), não permite valores nulos
    price = Column(Float, nullable=False)  # Coluna "price" (float), não permite valores nulos
    assessment = Column(Integer, nullable=False)  # Coluna "assessment" (inteiro), não permite valores nulos
