from pydantic import BaseModel


class bookSchema(BaseModel):
    title: str
    author: str
    year: int
    price: float
    isbn: str
    category: str
    assessment: int
