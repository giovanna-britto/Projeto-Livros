from pydantic import BaseModel  # Importa o BaseModel do Pydantic, usado para validação e estruturação de dados

# Classe base para definir os atributos comuns a todas as operações relacionadas aos livros
class BookBase(BaseModel):
    title: str  
    author: str  
    year: int  
    isbn: str  
    category: str  
    price: float  
    assessment: int  

# Classe usada para criação de livros (POST), herda os campos da BookBase
class BookCreate(BookBase):
    pass  # Não adiciona novos atributos, mas define o contexto como "criação"

# Classe usada para retornar livros ao cliente (GET), herda os campos da BookBase
class BookResponse(BookBase):
    id: int  # Identificador único do livro (gerado pelo banco de dados), tipo inteiro

    # Configuração adicional para permitir que o Pydantic converta objetos ORM (do SQLAlchemy) em JSON
    class Config:
        orm_mode = True
