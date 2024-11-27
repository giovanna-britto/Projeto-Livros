from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str
    category: str
    price: float
    assessment: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
