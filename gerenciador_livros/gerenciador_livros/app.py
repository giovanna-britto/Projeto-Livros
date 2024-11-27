from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from gerenciador_livros.schemas import BookCreate, BookResponse
from gerenciador_livros.models import Book
from gerenciador_livros.database import get_session

app = FastAPI()

# Endpoint para listar livros (GET)
@app.get("/books", response_model=list[BookResponse])
def get_books(session: Session = Depends(get_session)):
    books = session.query(Book).all()
    return books

# Endpoint para criar um livro (POST)
@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    try:
        new_book = Book(**book.dict())
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar livro: {str(e)}")

# Rota para atualizar um livro
@app.put('/books/{book_id}', response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, session: Session = Depends(get_session)):
    existing_book = session.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(existing_book, key, value)
    session.commit()
    session.refresh(existing_book)
    return existing_book

# Rota para deletar um livro
@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"message": "Book deleted successfully"}
